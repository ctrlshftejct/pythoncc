# Making Numeric Lists

# using the range() function
for value in range(0, 4):
    print(value)
    # notice that the range is off by one

for value in range(6):
    print(value)
    # don't have to pass two values, it defaults at 0

# using range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

# can also skip numbers in given range
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# make list of first 10 square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)