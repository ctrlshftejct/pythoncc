bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# access individual items in list
print(bicycles[0].title())

# modifying items in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list
motorcycles.append('honda')
print(motorcycles)

# inserting elements into a list (specific spot)
motorcycles.insert(2, 'bmw')
print(motorcycles)

# removing an item using the del statement
del motorcycles[2]
print(motorcycles)

# removing an item using the pop() method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
# pop method only "pops" off the last item of the list
# this would be useful for "last item bought" etc

# can also use pop to pull specific item
first_owned = motorcycles.pop(0)
print(f"\nThe first motorcycle I owned was a {first_owned.title()}.\n")
motorcycles.insert(0, 'ducati')

# removing an item by value
motorcycles.remove('ducati')
print(motorcycles)

# removing an item by value (as variable)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive to me.\n")

# organizing a list

# sorting a list permanently with sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(f"\nSorted List:\n\t{cars}")

# sorting list in reverse alphabetical order
cars.sort()
print(f"\nReverse Sorted:\n\t{cars}")

# temporarily sorting list with sorted()
print("\nCurrent list:")
print(cars)

print("Temporarily sorted list:")
print(sorted(cars))

print("Original List again:")
print(cars)

# printing a list in reverse order
print(cars)
print("\nprinting in reverse order, not alphabetical though.")
cars.reverse()
print(cars)

# finding length of list
print(f"Length of list: {len(cars)}")

# another way to find last item in list
print(cars[-1])
