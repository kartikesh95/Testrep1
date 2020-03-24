# Exercise 8: Printing, Printing

formatter = "{} {} {} {}"

# Print the positional arguments defined in format string as per the formatter variable
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) # Prints {} 16 times
# Same comment appplies here. Note that , is used to define the arguments in their own line - This helps keep the code neat.
print(formatter.format("Corona Corona", "Go Away", "Big Kartik", "Wants to work."))
