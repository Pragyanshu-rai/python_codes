# import the Artist class from Artist.py file or module
# Note:- The Artist file and the Atrwork file must be in the same folder or directory
from Artist import Artist

# you may also just import the Atrist file or module by typing:- import Atrist
# but then instead of typing the "this.artist = Artist()" class you must type "this.artist = Artist.Atrist()"  
class Artwork(): # does not inherits any other class
    
    # constructor for the Artwork class
    def __init__(this):
        
        this.artwork_title = None
        
        this.year_created = 0
        
        this.artist = Artist() # creating an artist object with the default values
    
    # defining a method to extract all the values an print it in the required format
    # method name print_data()
    
    def print_data(this):
        
        # checking if the artist is still alive or dead and creating the output string accordingly
        # true if the astist is dead
        if this.artist.year_of_death != -1:
            # converting year_of_birth and year_of_death into string
            # the rstrip() method removes white spaces from the right end of the string
            artist_line = this.artist.artist_name.rstrip() +' (' + str(this.artist.year_of_birth) + '-' + str(this.artist.year_of_death) + ')'
        
        # true if the artist still lives
        else:
            # converting year_of_death into string
            artist_line = this.artist.artist_name.rstrip() + ',' + ' born ' + str(this.artist.year_of_birth)
        
        # creating the output string for the artwork data by converting year_created into string and then concatenating it to the artwork title
        artwork_line = this.artwork_title.rstrip() + ', ' + str(this.year_created)
        
        # finally printing all the data
        print("Artist:", artist_line)
        print("Title:", artwork_line)

# main driver code

# first of all create an Artwork object

artwork = Artwork()

# Next get the input for the Artwork class object 

# name of the artist

artwork.artist.artist_name = input()

# year of birth and convert it into integer type

# int function takes numbers in string representation as an argument and returns the integer form of it

artwork.artist.year_of_birth = int(input())

# year of death and convert it into integer type

artwork.artist.year_of_death = int(input())

# artwork title

artwork.artwork_title = input()

# year created and convert it into integer type

artwork.year_created = int(input())

# calling the print_data method to print the data 

artwork.print_data()
