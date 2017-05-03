from qgis.gui import *
import urllib, urllib2
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
	data = get_data()
	header = get_header()
	req = urllib2.Request(request_string, data, header)
	response = urllib2.urlopen(req).read()
	info = json.loads(response)
	time.sleep(1)
	
	if info['display_name']:
		return info['display_name']
	else:
		return ""


def get_request_string(lat, lon):
	query = "format=json&lat="+str(lat)+"&lon="+str(lon)+"&zoom=18&addressdetails=1"
	request_string = "http://nominatim.openstreetmap.org/reverse?" + query
	return request_string


def get_data():
	values = {'name': get_env_variable('user_full_name'),
				   'language': 'Python'}
	data = urllib.urlencode(values) 
	return data


def get_header():
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
	header = {'User-Agent': user_agent}
	return header


def get_env_variable(var_name):
    """ Returns the value of the variable 'var_name' """
    active_layer = iface.activeLayer()
    return QgsExpressionContextUtils.layerScope(active_layer).variable(var_name) \
         or QgsExpressionContextUtils.projectScope().variable(var_name) \
         or QgsExpressionContextUtils.globalScope().variable(var_name)
