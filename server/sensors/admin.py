from sensors.models import *
from django.contrib import admin


def reg(mod):
    for i in mod:
        admin.site.register(i)

reg([
    Sensor,
    SensorType,
    Reading,
])