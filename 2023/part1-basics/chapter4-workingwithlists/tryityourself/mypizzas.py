# my pizzas, your pizzas

# original list
pizzas = ['pepperoni', 'sausage', 'cheese', 'margherita']

# make a copy of list called friends_pizzas
friend_pizzas = pizzas[:]

# add a new pizza to the original list
pizzas.append('chicken bbq')

# add a different pizza to the list friend_pizzas
friend_pizzas.append('kimchi')

# prove that you have two separate lists
print("My favorite pizzas are:")
print(pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)