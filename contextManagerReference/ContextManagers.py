# context managers are used to manage and handle the resource (opening and closing)

FILE_NAME: str = "textFile.txt"
FILE_MODE: str = "w"
FILE_DATA: str = """Climes shamed was to ah one fountain memory.
Woe yea my him een. Een a and before night it where.
Uncouth this though take than wight concubines a,
way native.

-- by ContextManagers"""

with open(FILE_NAME, FILE_MODE) as file_handle:
    file_handle.write(FILE_DATA)
