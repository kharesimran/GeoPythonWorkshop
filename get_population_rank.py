@qgsfunction(args='auto', group='Custom', referenced_columns=['pop_max'])
def get_population_rank(feature, parent):
	"""
	Returns the population rank of a feature as defined in
	http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-populated-places/
	Usage: get_population_rank()
	"""
	pop = feature['pop_max']
	if pop > 10000000:
		pop_rank = 14
	elif pop > 5000000:
		pop_rank = 13
	elif pop > 1000000:
		pop_rank = 12
	elif pop > 500000:
		pop_rank = 11
	elif pop > 200000:
		pop_rank = 10
	elif pop > 100000:
		pop_rank = 9
	elif pop > 50000:
		pop_rank = 8
	elif pop > 20000:
		pop_rank = 7
	elif pop > 10000:
		pop_rank = 6
	elif pop > 5000:
		pop_rank = 5
	elif pop > 2000:
		pop_rank = 4
	elif pop > 1000:
		pop_rank = 3
	elif pop > 200:
		pop_rank = 2
	elif pop > 0:
		pop_rank = 1
	else:
		pop_rank = 1
	return pop_rank
