# Exercise 5: More Variables and Printing

name = 'Kartikesh A. Nadar'
age = 37
height_inches = 68 # inches
height_cms = round (height_inches * 2.54)
weight_lbs = 198 # lbs
weight_kg = round (weight_lbs / 2.2)
eyes = 'Black'
teeth = 'White'
hair = 'Black & White'

print(f"Let's talk about {name}.")
print(f"He's {height_inches} inches or in other words {height_cms} cms tall.")
print(f"He's {weight_lbs} pounds or in other words {weight_kg} kilograms heavy.")
print(f"Actually that's a bit on the heavy side.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_inches + weight_lbs
print(f"If I add {age}, {height_inches}, and {weight_lbs} I get {total}.")
