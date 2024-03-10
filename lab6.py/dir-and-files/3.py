import os

def analyzePath(givenPath):
    if os.path.exists(givenPath):
        print("The path exists.")
        filename = os.path.basename(givenPath)
        directory = os.path.dirname(givenPath)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("The path does not exist.")
givenPath = 'C:\KBTU\PP2\week1'
analyzePath(givenPath)