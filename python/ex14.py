from sys import argv
script , user_name = argv
prompt = ">"
print(f"hi {user_name}, I'am {script} script.")
print("I would like to ask you a few questions.")
print(f"Do you like me {user_name}?")
like=input(prompt)
print(f"Where do you live {user_name}?")
lives=input(prompt)
print("What kind of computer do you have?")
comp=input(prompt)
print(f"""
Alright, so you said {like} about liking me.
You live in {lives}, not sure where it is.
And you have a {comp}. Nice.
""")
