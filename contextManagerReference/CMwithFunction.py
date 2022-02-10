# function implementation of context managers

from contextlib import contextmanager

FILE_NAME: str = "textFile.txt"
FILE_MODE: str = "w"
FILE_DATA: str = """
Widerklang der wiederholt die und ihr tränen einst die. Der was und fühlt schwebet die. Lied 
drängt ihr euch busen noch entwöhntes wahn wieder, der meinem entwöhntes wird nicht lieb lieb 
nun erste meinem, wird dunst die blick was der.

-- by CMwithFunction"""


@contextmanager
def open_file(file_name: str, file_mode: str = 'r'):
    
    try:
        file = open(file_name, file_mode)
        yield file
    
    except Exception as error:
        print("OPEN FILE ERROR", error)
    
    finally:
        file.close()

with open_file(FILE_NAME, FILE_MODE) as file_handler:
    file_handler.write(FILE_DATA)