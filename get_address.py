import urllib2
import json
import time


@qgsfunction(args='auto', group='Custom', referenced_columns=['latitude', 'longitude'])
def get_address(feature, parent):
	""" 
	Use Nominatim's API for reverse geocoding.
	i.e., given the latitude and longitude of a feature, get the address.
	Usage: get_address()
	"""
	lat = feature['latitude']
	lon = feature['longitude']
	request_string = get_request_string(lat, lon)
	header = get_header()
	req = urllib2.Request(url=request_string, headers=header)
	response = urllib2.urlopen(req).read()
	info = json.loads(response)
	time.sleep(1)
	
	if info['display_name']:
		return info['display_name']
	else:
		return ""


def get_request_string(lat, lon):
	query = "format=json&lat="+str(lat)+"&lon="+str(lon)
	request_string = "http://nominatim.openstreetmap.org/reverse?" + query
	return request_string


def get_header():
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
	header = {'User-Agent': user_agent}
	return header