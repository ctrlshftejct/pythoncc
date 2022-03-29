# USING MULTIPLE elif BLOCKS

# You can use as many 'elif' blocks in your code as you like. For example, if the amusement park were to implement a discount for seniors, you could add one more conditional test to the code to determine whether someone qualified for the senior discount. Let's say that anyone 65 or older pays half the regular admission, or $20:

age = 66

if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
  price = 40
else:
  price = 20

print(f"Your admission cost is ${price}.")
