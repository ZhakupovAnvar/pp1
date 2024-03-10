import os

a = open(r"C:\KBTU\PP2\week1\lab6.py\dir-and-files\primer.txt")
cnt = 0
for lines in a:
    cnt += 1
print(f"The file has {cnt} lines")