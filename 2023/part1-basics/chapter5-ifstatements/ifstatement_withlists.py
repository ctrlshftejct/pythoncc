# checking for special items
# using if statments and for loops

requested_toppings = ['pepperoni', 'green peppers', 'sausage']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!\n")

# what if you run out of peppers?

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")