def copyFile(sourceFile, destinationFile):
    try:
        with open(sourceFile, 'r') as source:
            with open(destinationFile, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except Exception as e:
        print("An error occurred:", str(e))
sourceFile = 'primer.txt'
destinationFile = 'primer2.txt'

copyFile(sourceFile, destinationFile)