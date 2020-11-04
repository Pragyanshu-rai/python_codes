print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")
d = input("> ")
if d == "1":
	print("There's a gaint bear here eating a cheese cake")
	print("What do you do?")
	print("1. Take the cake.")
	print("2.Scream at the bear.")
	b = input("> ")
	if b== "1":
		print("The bear eats your face off. Good Job!")
	elif b =="2":
		print("The bear eats your legs off. Good Job!")
	else:
		print(f"Well, doing {b} is probably better")
		print("Bear runs away")
elif d == "2":
	print("You stare into the endless abyss at cthulhu's retina.")
	print("1. Blueberries")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")
	i = input("> ")
	if i == "1" or i == "2":
		print("Your body survives powered by a mind of jello.")
		print("Good Job!")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good Job!")
#else if True: invalid syntax
#	print("\n\tyo\n")
else:
	print("You stumble around and fall on a knife and die. Good Job!")
