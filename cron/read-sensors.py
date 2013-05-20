import glob
import re

import sys
sys.path.append("../env")
sys.path.append("../server/")

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pocketServ.settings")

from sensors.models import *

'''
    SUMMARY

loop through 1 wire devices folder and return that data in an
{
    'id': 'value'
}
format. Right now, this is just for temperature sensors, and may need to be updated to
work with other types of devices.


'''


'''
    SETUP
'''

w1_list = glob.glob("/sys/bus/w1/devices/*")
w1_folder_regex = re.compile('\d+-\d+')

sensor_reading_regex = re.compile('\ze[\d]+\n')


# Sample data
#w1_list = ['foobar', '1234567890-2345678900987654321']
# end sample data

'''
    RUN
'''


w1_list = filter(w1_folder_regex.search, w1_list)

for sensor in w1_list:
    sensor_serial = None
    sensor_reading = None

    print sensor
    sensor_serial = w1_folder_regex.search(sensor).group(0)

    try:
        sensor = Sensor.objects.get(serial=sensor_serial)
    except Sensor.DoesNotExist:
        Sensor(serial=sensor_serial)
        Sensor.save()
        sensor = Sensor

    with open(sensor + '/w1_slave') as f:
        sensor_reading = f.readlines()

    sensor_reading = sensor_reading_regex.search(sensor_reading).group(0)

    Reading(sensor=sensor, value=sensor_reading)

print sensors
