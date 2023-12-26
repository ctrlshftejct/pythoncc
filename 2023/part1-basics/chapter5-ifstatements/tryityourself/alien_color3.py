# Alien Colors #3

# turn if-else chain into if-elif-else
points = 0
# define alien_color
alien_color = 'green'
# if green, 5 points
if 'green' in alien_color:
    print("5 points.")
    points += 5
# if yellow, 10 points
elif 'yellow' in alien_color:
    print("10 points.")
    points += 10
# if red, 15 points
else:
    print("15 points.")
    points += 15

# make three versions of program
alien_color = 'yellow'

if 'green' in alien_color:
    print("5 points.")
    points += 5
elif 'yellow' in alien_color:
    print("10 points.")
    points += 10
else:
    print("15 points.")
    points += 15

alien_color = 'red'

if 'green' in alien_color:
    print("5 points.")
    points += 5
elif 'yellow' in alien_color:
    print("10 points.")
    points += 10
else:
    print("15 points.")
    points += 15

print(f"{points} points total.")