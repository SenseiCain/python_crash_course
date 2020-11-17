# -- FUNCTIONS --
# Same indention notation as for loops
# Define a Fn with def
# Snake case

def greet(name):
	print(f'Hello, {name.title()}!')
# greet('Christian')

# Positional arguments
def greet_with_sirname(name, sirname='Mr/Mrs'):
	print(f'Greetings {sirname}. {name}')
# greet_with_sirname('Christian', 'Mr')

# Key Name arguments
# Position doesn't matter here
# Define on execution!!!
# greet_with_sirname(sirname='Mr', name='Christian')

# Return Value
num = 2
def square(num):
	return num**2
# print(square(num))

# Optional args
# Takes advantage of Python using non-empty strings as True
def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = f'{first_name} {middle_name} {last_name}'
	else:
		full_name = f'{first_name} {last_name}'
	return full_name.title()
# print(get_formatted_name('Christian', 'Cain'))

# Functions & immutable lists
# function_name(list[:])

# Passing in an arbitrary amount of args
def make_pizza(*toppings):
	for topping in toppings:
		print(topping)
# make_pizza('cheese')
# make_pizza('cheese', 'pepperoni', 'mushrooms')

# Keyword Args
# Use when unsure of how many key-values pairs will be passed in
# **kwargs
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
# print(build_profile('Christian', 'Cain', hometown='Richwood'))

