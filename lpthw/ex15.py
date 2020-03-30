# Exercise 15 - Reading Files

#Imports the argv list from the sys module in python
#from sys import argv

#sets two argument variables in argv - One is the scriptname and other is the filename
#script, filename = argv

filename = input("Please provide the filename: ")

#Opens the file called filename which is provided by the user
txt = open(filename)

print(f"Here's your filename: {filename}")
#Reads the contents of the file stored in the txt variable. And then prints it to the terminal
print(txt.read())

txt.close()
