import os

path = r'C:\KBTU\PP2\week1' 
a = os.listdir(path)
for sled in a:
    full_path = os.path.join(path, sled)
    print('Exists:', os.access(full_path, os.F_OK))
    print('Readable:', os.access(full_path, os.R_OK))
    print('Writable:', os.access(full_path, os.W_OK))
    print('Executable:', os.access(full_path, os.X_OK))
    print()