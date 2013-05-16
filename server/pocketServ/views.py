from django.shortcuts import render_to_response
from django.template import RequestContext
from sensors.models import *


def home(request):
    sensors = Sensor.objects.all()
    return render_to_response(
        'home.html',
        {
            'sensors': sensors
        },
        context_instance=RequestContext(request))
