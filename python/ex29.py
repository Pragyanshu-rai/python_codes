people = 20
cats = 30
dogs = 15
if people < cats:
	print(f"Too many cats {cats}! The world is doomed!")
elif people>cats:
	print(f"Not many cats {cats}! The world is saved!")
if people<dogs:
	print(f"The world is drooled on! {dogs}")
elif people>dogs:
	print("The world is dry! {}".format(dogs))
dogs+=5
if people>=dogs:
	print(f"people {people} are grater than equal to dogs {dogs}")
if people<=dogs:
	print(f"people {people} are less than equal to dogs {dogs}")
if people==dogs:
	print(f"people {people} are dogs. {dogs}")
if True or False:
	print("\n\tor\n")
if True and not False:
	print("\n\tand\n")
if True and not(False):
	print("\n\tand not\n")
