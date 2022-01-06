flavor ="apple pie"

first_three_letters = flavor[0]+flavor[1]+flavor[2]

print(first_three_letters)

print(flavor[0:3])

print(flavor.upper())
print(flavor.lower())
flavor = flavor.upper()
print(flavor)

#to remove whitespace from a string
name="Surendra KUmar "
print(name.rstrip()) #removing the whitespace on both side of the string
name = "   Surendra KUmar  "
print(name.lstrip())  #removing the whitespace on the left side of the strring
print(name.rstrip()) #removing the whitespace on the right side of the string


startship = "Enterprise"

print(startship.startswith("en"))

print(startship.endswith("rise"))

