import glob
import os

names = glob.glob("*.jpeg")
for name in names:
    new_name = name.split('.')[0]+'_PapV.jpg'
    print(new_name)
    os.renames(name, new_name)
