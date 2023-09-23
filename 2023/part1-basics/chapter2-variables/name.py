# strings and how to manipulate them

name = 'andrew harvey'
print(name.title())
print(name.upper())

# using variables in strings

first_name = 'andrew'
last_name = 'harvey'

#using format method "f"
print(f"{first_name} {last_name}")
full_name = f"{first_name} {last_name}"
print(f"{full_name.title()}")

#stripping white space
favorite_language = 'python '
print(favorite_language.rstrip())