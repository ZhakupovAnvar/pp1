import os
p=(r"C:\KBTU\PP2\week1\lab6.py\dir-and-files\shdel.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("the file does not exist")