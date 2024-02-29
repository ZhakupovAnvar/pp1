import re

def Bigfinder(n):
    a=(r'[A-Z][a-z]+')
    b=re.findall(a,n)
    return b

n=str(input())
print("I found:",Bigfinder(n))