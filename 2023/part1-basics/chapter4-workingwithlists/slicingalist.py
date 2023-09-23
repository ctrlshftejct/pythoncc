# slicing a list

names = ['andrew', 'martina', 'michael', 'florence', 'eli']
print(names[0:3])

# looping through a slice

print("Here are the first three players on my team:")
for name in names[:3]:
    print(name.title())