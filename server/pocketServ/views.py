from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.core import serializers

from sensors.models import *

import json


def home(request):
    sensors = Sensor.objects.all()
    return render_to_response(
        'home.html',
        {
            'sensors': sensors
        },
        context_instance=RequestContext(request))


def ajax_gauge_update(request):
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
