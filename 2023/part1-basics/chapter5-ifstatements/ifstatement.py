# simple if statement

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# if and if/else conditionals

age = 35
if age >= 18:
    print("You're old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("You are not old enough")

# if-elif-else chain

# admission for anyone under age 4 is free.
# admission for anyone between the ages of 4 and 18 is $25
# admission for anyone 18 or older is $40.

age = 12

if age < 4:
    print("Your admission is free of charge!")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40.")

# using variables and multiple elif blocks

age = 66

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40

if price == 0:
    print("Your admission is free of charge!")
else:
    print(f"Your admission cost is ${price}.")

# sometimes multiple if statements are necessary

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
