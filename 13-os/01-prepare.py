import os
import shutil

path = input("Where do you want your project?")

os.mkdir(path)
print("Copying file: ", __file__)
shutil.copy(__file__, path)
