# class implementation of context managers


from io import TextIOWrapper

FILE_NAME: str = "textFile.txt"
FILE_MODE: str = "w"
FILE_DATA: str = """E d'angoscia apparire cominciamento noi quella, prieghi quale procuratore
non il al e potremmo intendo, cosa ripararci prestasse maravigliose maravigliose nostra la, 
oportune non sono intendo in suo. Come spezial facitore speranza a di, che piaceri cosa fa e 
il.

-- by CMwithClass"""


class OpenFile():

    def __init__(self, file_name: str, file_mode: str = 'r') -> None:
        self.__file_name = file_name
        self.__file_mode = file_mode

    def __enter__(self) -> TextIOWrapper:
        self.__file = open(self.__file_name, self.__file_mode)
        return self.__file

    def __exit__(self, exc_type, exc_val, traceback) -> None:
        self.__file.close()


with OpenFile(FILE_NAME, FILE_MODE) as file_handle:
    file_handle.write(FILE_DATA)
