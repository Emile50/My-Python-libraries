"""-----------------Requirements----------------"""
import os
import sys
"Enforce python version 3.9+ so that built in typing enforcement just works without Typing and typeguard modules"
required_version = (3, 9)
if sys.version_info < required_version:
    raise Exception(f"This script requires Python {required_version[0]}.{required_version[1]} or higher. Current version is {sys.version_info[0]}.{sys.version_info[1]}")

#current_dir = os.getcwd()
#filePath = os.path.join(path, fileName)

""" ---to use the type enforcement module:-----
@runtime_validation
def add_numbers(x: int, y: int) -> int:
    return x+y
    
try:
    print(add_numbers(3, "five"))
except TypeError as e:
    print("Error:", e)

#typing a tuple:
tuple[int, ...] #a tuple of all ints
tuple[int, str] # first element int, second str
list[int, str] #all elements str or int
"""

def create_database(db_name: str, columns: tuple[str, ...], db_path: str = "") -> None:
    db_path = os.path.join(path, file_name) 
    with open(db_path, "w") as new_file:
        header = f"""Text database by Émile Lareau
---===Configuration===---
Allow duplicate entries: True
Columns = {columns}

---===Entries===---
"""
        new_file.write(header)
        
        
def load_database(path):
    pass

create_database("data-based test", ("id", "name", "basedness"))
    
    
