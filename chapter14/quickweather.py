#! python3
# quickweather.py - prints the weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.

if len(sys.argv) < 2:
	print ('Usage : quickweather.py location')
	sys.exit()
location = ' '. join(sys.argv[1:])

# Download the JSON datafrom OpenWeatherMap.org's API.

url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data in a python variable.

weatherData = json.loads(response.text)

# Print weather descriptions.

w = weatherData['list']
print ('Current weather in %s :' % (location))
print (w[0]['weather'][0]['main'], w[0]['weather'][0]['description'])
print ()
print ('tomorrow:')
print (w[1]['weather'][0]['main'], w[1]['weather'][0]['description'])
print ()
print ('Day after tomorrow:')
print (w[2]['weather'][0]['main'], w[2]['weather'][0]['description'])

