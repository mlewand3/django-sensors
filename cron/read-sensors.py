import glob
import re

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

sensors = []
sensor_serial_regex = re.compile('\ze\/.*')


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

    with open(sensor + '/w1_slave') as f:
        sensor_reading = f.readlines()

    sensor_serial = w1_folder_regex.search(sensor).group(0)

    sensors.append({
        'sensor': sensor_serial,
        'reading': sensor_reading,
    })

print sensors
