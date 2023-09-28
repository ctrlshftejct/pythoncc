# conditional tests

# the heart of every if statement is a conditional
# testing for equality is case sensitive

# checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# numerical comparisons

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# other mathematical comparisons
if answer < 42:
    print("Too low! The answer should be higher!")

# checking multiple conditions at once
# can also choose 'and' instead of 'or'
if answer < 42 or answer > 42:
    print("Either too high or too low!")

# checking whether a value is in a list
# using 'in'
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("True")
if 'pepperoni' in requested_toppings:
    print("True")
else:
    print("False")

# checking whether a value is NOT in a list
# using 'not in'
banned_users = ['andrew', 'callie', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# boolean expressions
# boolean values are either 'True' or 'False'

game_active = True
can_edit = False