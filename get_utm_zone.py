from qgis.core import *
from qgis.gui import *
import math

@qgsfunction(args=0, group='Populated places', usesgeometry=True)
def get_utm_zone(value1, feature, parent):
	""" 
	Returns the UTM zone that each feature lies in.
	Usage: get_utm_zone()
	"""
	geom = feature.geometry()
	longitude = geom.asPoint().x()
	latitude = geom.asPoint().y()
	zone_number = math.floor(((longitude + 180) / 6) % 60) + 1

	if latitude >= 0:
		zone_letter = 'N'
	else:
		zone_letter = 'S'

	return '%d%s' % (zone_number, zone_letter)
