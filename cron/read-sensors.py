import glob, re

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



# Sample data
#w1_list = ['foobar', '1234567890-2345678900987654321']
# end sample data

'''
    RUN
'''

print w1_list

w1_list = filter(w1_folder_regex.search, w1_list)

print w1_list
