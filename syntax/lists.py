# -- LISTS --
# Python's approach to Arrays
# Should be named plural


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0]) // => trek
# print(bicycles[-1]) // => specialized
# print(f'My first bicycle was a {bicycles[0].title()}')

motorcycles = ['honda', 'yamaha', 'suzuki']

# Change at index
motorcycles[0] = 'ducati'

# Add to end
motorcycles.append('harley')

# Insert at index
motorcycles.insert(0, 'BMW')

# Delete at index
del motorcycles[-1]

# Remove el & return it
# - If no arg, then removes last el
popped_motorcycle = motorcycles.pop(0)
# print(popped_motorcycle) // => BMW

# Remove specific Value
motorcycles.remove('ducati')

# Sorting lists
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort() // => alphabetical order
# cars.sort(reverse=True) // => reverse alphabetical order

# Non mutation sort
sorted_cards = sorted(cars)

# Reverse array
cars.reverse()

# Find length
print(len(cars))