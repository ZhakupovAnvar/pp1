import re

def finder(n):
    a=(r'[a-z]+_[a-z]+')
    b=re.findall(a,n)
    return b

n=str(input())

print("I found:", finder(n))