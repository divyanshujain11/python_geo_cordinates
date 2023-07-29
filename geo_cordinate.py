# get gps coordinates from geopy
import json

# import urlopen from urllib.request
from urllib.request import urlopen

# url to get ipaddress
urlopen("http://ipinfo.io/json")

# load data into array
data = json.load(urlopen("http://ipinfo.io/json"))

# lattitude
lat = data['loc'].split(',')[0]

# longitude
lon = data['loc'].split(',')[1]

print(lat, lon)
