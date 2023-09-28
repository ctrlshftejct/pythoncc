# defining a tuple
'''
lists are for things that can change throughout a program
tuples are concrete, they are lists of items that
cannot, or we don't want to change.
'''
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# tuples defined by the presence of a comma
my_t = (3,)

# looping through tuple
for dimension in dimensions:
    print(dimension)

# writing over a tuple
# you can't change it but you can overwrite it
print(f"original dimensions = {dimensions}")
dimensions = (400, 100)
print(f"new dimentions = {dimensions}")
