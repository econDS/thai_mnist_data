import glob
import os

names = glob.glob("*.jpg")
for name in names:
    new_name = name.split('_')[0]+'_BoCF.jpg'
    print(new_name)
    os.renames(name, new_name)
