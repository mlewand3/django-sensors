from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from sensors.models import *

import json
import glob
import re


def home(request):
    sensors = Sensor.objects.all()
    return render_to_response(
        'home.html',
        {
            'sensors': sensors
        },
        context_instance=RequestContext(request))


def ajax_gauge_update(request):
    w1_list = glob.glob("/sys/bus/w1/devices/*")
    w1_folder_regex = re.compile('\d+-\d+')
    sensor_reading_regex = re.compile('[\d]+\n')
    w1_list = filter(w1_folder_regex.search, w1_list)
    for sensor in w1_list:
        sensor_serial = None
        sensor_reading = None

        sensor_serial = w1_folder_regex.search(sensor).group(0)

        try:
            sensor_obj = Sensor.objects.get(serial=sensor_serial)
        except Sensor.DoesNotExist:
            sensor_obj = Sensor(serial=sensor_serial)
            sensor_obj.save()

        with open(sensor + '/w1_slave') as f:
            sensor_reading = f.readlines()

        sensor_reading = ' '.join(sensor_reading)
        sensor_reading = sensor_reading_regex.search(sensor_reading).group(0)

        reading = Reading(sensor=sensor_obj, value=sensor_reading)
        reading.save()

    sensors = Sensor.objects.all()
    latest_readings = []
    json_out = ''
    for sensor in sensors:
        latest_readings.append({
            'name': sensor.title,
            'last-reading': (float(sensor.latest_reading()) / 1000),
        })
    json_out = json.dumps(latest_readings)
    return HttpResponse(json_out, content_type="application/json")
