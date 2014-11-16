from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from sensors.models import *
from sensors import settings

import json


def home(request):
    sensors = Sensor.objects.all()
    return render_to_response(
        'home.html',
        {
            'sensors': sensors
        },
        context_instance=RequestContext(request))


def update_sensors(request):
    w1_list = filter(settings.W1['FOLDER_REGEX'].search, settings.W1['LIST'])
    for sensor in w1_list:
        sensor_serial = None
        sensor_reading = None

        sensor_serial = settings.W1['FOLDER_REGEX'].search(sensor).group(0)

        try:
            sensor_obj = Sensor.objects.get(serial=sensor_serial)
        except Sensor.DoesNotExist:
            sensor_obj = Sensor(serial=sensor_serial)
            sensor_obj.save()

        with open(sensor + '/w1_slave') as f:
            sensor_reading = f.readlines()

        sensor_reading = ' '.join(sensor_reading)
        sensor_reading = settings.W1['READING_REGEX'].search(sensor_reading).group(0)

        reading = Reading(sensor=sensor_obj, value=sensor_reading)
        reading.save()


def ajax_gauge_update(request):
    '''

    '''

    sensors = Sensor.objects.all()
    latest_readings = []
    for sensor in sensors:
        latest_readings.append({
            'name': sensor.title,
            'last-reading': (float(sensor.latest_reading()) / 1000),
        })
    return HttpResponse(
        json.dumps(latest_readings),
        content_type="application/json"
    )
