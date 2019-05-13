from sys import argv
# there things that equal something
script, user_name = argv
prompt = '> '
# your r=writes questions you want to be answered
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)
# i woner what those quation marks do
print(f"""
Alright, so you said {likes} about liking me.
you live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
