import os

def listDirectoriesFiles(path):
    print("Directories:")
    for whod in os.listdir(path):
        if os.path.isdir(os.path.join(path, whod)):
            print(whod)
    print("\nFiles:")
    for whod in os.listdir(path):
        if os.path.isfile(os.path.join(path, whod)):
            print(whod)
    print("\nAll:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))
path = 'C:\KBTU\PP2\week1\lab6.py'

listDirectoriesFiles(path)