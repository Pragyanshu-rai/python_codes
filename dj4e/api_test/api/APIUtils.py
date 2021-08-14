# This the APIUtils file, it contains extra functions for opertaions on json data and models

# from django.contrib.auth.models import User
# from .models import Student


# userUpdate function takes a user object and python data as argument and updates the data in user model and then returns the user object  
def userUpdate(user, items):

 if "first_name" in items.keys():
  if items["first_name"] != None :
		 user.first_name = items.pop("first_name")
 if "last_name" in items.keys():
  if items["last_name"] != None :
		 user.last_name = items.pop("last_name")
 if "email" in items.keys():
  if items["email"] != None :
		 user.email = items.pop("email")
 if "password" in items.keys():
  if items["password"] != None :
		 user.password = items.pop("password")
 
 user.save()
 return user

 