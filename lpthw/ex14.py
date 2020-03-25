# Exercise 14 - Prompting and Passing

from sys import argv

script, user_name, age= argv
prompt = '~ '

print(f"Hi {user_name}. I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do yo like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
Computer = input(prompt)

print(f"""
Alright. so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You are {age} years old.
And you have a {Computer} computer. Nice.
""")
