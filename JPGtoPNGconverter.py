#To use, enter on terminal:
#JPGtoPNGconverter.py + "current_folder_name/" + "new_folder_name/"
#For example: JPGtoPNGconverter.py Pokedex/ new/



#Modules
import sys
import os
from PIL import Image

#On terminal, these variables allow you to grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]


#check if the new/ path exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

#check every jpg item on the directory to convert to png
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.png', 'png')
    print(f'{filename} has been converted :D')