@qgsfunction(args='auto', group='Custom', referenced_columns=['featurecla', 'pop_max'])
def is_populous_capital(input_pop, feature, parent):
	""" 
	Returns True for all country capitals with 
	population greater than a user-defined number (input_pop).
	Usage: is_populous_capital(200000)
	"""
	is_capital = feature['featurecla'] == 'Admin-0 capital'
	is_populous = feature['pop_max'] > input_pop
	return is_capital and is_populous
