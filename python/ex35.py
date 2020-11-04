from sys import exit
def gr():
	print("This room is full of gold. how much do you take?")
	c = input("> ")
	if '0' in c or '1' in c:
		hm = int(c)
	else:
		d("Man, learn to type a number.")
	if hm < 50:
		print("Nice, you are not greedy, you win!")
		exit(2)
	else:
		d("You greedy basterd")
def br():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bm = False
	while True:
		c = input("> ")
		if c == "take honey":
			d("The bear looks at you then slaps your face off.")
		elif c == "taunt bear" and not bm:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bm = True
		elif c == "open door" and bm:
			gr()
		else:
			print("I got an idea what that means.")
def cr():
	print("Here you see the greatest evil cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")
	c = input("> ")
	if "flee" in c:
		st()
	elif "head" in c:
		d("Well that was tasty")
	else:
		cr()
def d(w):
	print(w,"Good job!")
	exit(3)
def st():
	print("You are in a dark room.")
	print("There is a door to your right and left")
	print("Which one do you take?")
	c = input("> ")
	if c =="left":
		br()
	elif c =="right":
		cr()
	else:
		d("You stumble around the room until you starve.")
st()
