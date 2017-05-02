from qgis.core import *
from qgis.gui import *


@qgsfunction(args='auto', group='Populated places')
def select_populous_capitals(input_pop, field1, field2, feature, parent):
    """ 
    Select all the capital cities with 
    population greater than a user-defined number (input_pop).
	Usage: select_populated_capitals('20000', "featurecla", "pop_max")
    """
    is_capital = feature['featurecla'] == 'Admin-0 capital'
    is_populated = int(feature['pop_max']) > int(input_pop)
    return is_capital and is_populated
