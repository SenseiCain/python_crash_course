# -- IF Statements --
# Similar indenting notation to for loops
# if, elif, else


cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
# 	if len(car) == 3:
# 		print(f'{car.title()} has 3 letters!')
# 	else:
# 		print(f'{car.title()} does not have 3 letters!')

# Case is taken into account when comparing
car = 'Audi'
# car == 'audi' // => False

# and = &&
# or = ||

band_users = ['Tim', 'Bill', 'Jessica']
# if 'Christian' not in band_users:
# 	print(f'Christian is safe to go in!')

# If vs. elif
# 	- Multiple if's will test all conditions
# 	- Multiple elif's will stop at the first met condition

empty_list = []
# if empty_list:
# 	print('list is not empty')
# if not empty_list:
# 	print('list is empty')