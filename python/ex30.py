people = 30
cars = 40
trucks = 15
if cars>people:
	print("We should take the cars {}.".format(cars))
elif cars<people:
	print("We should not take the cars.")
else:
	print("We can'trucks decide.")
if trucks>cars:
	print("That's too many trucks {}".format(trucks))
elif trucks<cars:
	print(f"Maybe we colud take the trucks {trucks}.")
else:
	print("We still can'trucks decide.")
if people>trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")
