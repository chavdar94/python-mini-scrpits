import os

'''
Removes white-spaces from filenames
'''

dir_path = ""  # full path to folder containing files

for dirpath, dirnames, filenames in os.walk(dir_path):
    for f in filenames:
        new_filename = f.replace(" ", "")
        os.rename(os.path.join(dirpath, f), os.path.join(dirpath, new_filename))
