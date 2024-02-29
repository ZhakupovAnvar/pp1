import re

def delenie(n):
    a=(r'[A-Z][a-z]*')
    b=re.findall(a,n)
    print(b)

n=str(input())
delenie(n)