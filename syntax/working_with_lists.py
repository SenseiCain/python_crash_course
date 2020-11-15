# -- Workign with Lists --
# list [] == let
# tuples () == const (sort of)


magicians = ['alice', 'david', 'carolina']

# for magician in magicians:
# 	print(magician)

# A LOT CLEANER THAN JS!!!
# for(let i = 0; i < magicians.length; i++){
# 	console.log(magicians[i]);
# }

# Range
# for value in range(1, 5):
# 	print(value)
# // => 1, 2, 3, 4

numbers = list(range(6))
# print(numbers) // => [1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2))
# print(even_numbers) // => [2, 4, 6, 8]

fib_numbers = [1, 1]
for value in range(8):
	new_num = fib_numbers[-1] + fib_numbers[-2]
	fib_numbers.append(new_num)
# print(fib_numbers) // => [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# print(min(numbers)) // => 0
# print(max(numbers)) // => 5
# print(sum(numbers)) // => 15


# -- list comprehension --
# Similiar to map

squares = [value**2 for value in range(5)]
# print(squares) // => [0, 1, 4, 9, 16]

first_three_squares = squares[:3]
last_threeSquares = squares[-3:]

squares_copy = squares[:]


# -- Tuples --
# Immutable lists, similar to JS const
# Protects against single value assignment
# Doesn't protect from complete resassignment

new_tuple = (1, 2, 3)
single_tuple = (3,)
# new_tuple[0] = 4 // => TypeError
# new_tuple = (2, 4, 6) // => Perfectly fine???

