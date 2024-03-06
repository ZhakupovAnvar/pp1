some = str(input())
low, upp = 0, 0
for char in some:
    if(char.islower()):
        low += 1
    if(char.isupper()):
        upp +=1

print(low, upp)