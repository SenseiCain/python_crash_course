# -- DICTIONARIES --
# Connect pieces of related info
# dictionaries == objects == hashes

alien_0 = {'color': 'green', 'planet': 'zion'}
# print(alien_0['color']) //=> green

# Keys are kept in the same order they're added
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25

# Overwriting values
alien_0['color'] = 'purple'

# Delete  key/value
del alien_0['planet']

# Get method
# Optional - set default return, or returns NONE
# DOESN'T SET DEFAULT VALUE!!
# print(alien_0.get('name', 'Blinky'))

# -- Looping through dictionaries --
# 	1) for key, value in alien_0
# 	2) for key in alien_0.keys()
# 	3) for key in alien_0 - Same as above!
# 	4) for value in alien_0.values()

# set() makes list unique!

list_of_ranges = []
for value in range(6):
	new_dict = {'range': value}
	list_of_ranges.append(new_dict)
# print(list_of_ranges[3]['range']) // => 3


# -- Nested data structures --
complex_dict = {
	'first': {
		'name': 'Christian',
		'age': 25,
		'hobbies': ['cooking', 'skating', 'hiking']
	}
}

# print(complex_dict['first']['hobbies'][2]) // => 'hiking'