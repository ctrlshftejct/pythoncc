# stages of life

# define variable age
age = int(input("What is your age? "))

# Less than 2 = baby
if age < 2:
    print("You're a baby.")
# 2 and less than 4 = toddler
elif age == 2 and age < 4:
    print("You're a toddler.")
# 4 and less than 13 = kid
elif age == 4 and age < 13:
    print("You're a kid.")
# 13 and less than 20 = teenager
elif age == 14 and age < 20:
    print("You're a teenager.")
# 20 and less than 65 = adult
elif age == 20 and age < 65:
    print("You're an adult.")
# 65 or older = elder
else:
    print("You're old as fuck.")