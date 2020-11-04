states = {
			'ts':'Telangana',
			'up':'Uttar Pradesh',
			#'ap':'Arunachal Pradesh',
			'mh':'Maharashtra',	
 		 	"mp":"Madhya Pradesh",
		 }
cities = {
		    'Telangana':'Hyderabad',
			'Madhya Pradesh':'Bhopal',
			'Uttar Pradesh':'Varanasi',
		 }
cities['Maharashtra'] = 'Mumbai'
print("-"*10)
print("Maharashtra states has :",cities["Maharashtra"])
print("-"*10)
for i,j in list(states.items()):
	print(f"state {i} is : {j}")
	print(f"city is : {cities[j]}")
