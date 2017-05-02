from qgis.core import *
from qgis.gui import *


@qgsfunction(args='auto', group='Populated places')
def get_change_in_population(field1, field2, feature, parent):
	"""
	Returns the change in population for each feature.
	Usage: get_change_in_population("pop_max", "pop_min")
	"""
	max_pop = feature['pop_max']
	min_pop = feature['pop_min']
	change_in_pop = float(max_pop - min_pop) / min_pop
	return "{0:.2f}".format(change_in_pop)
