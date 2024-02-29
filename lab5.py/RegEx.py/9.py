import re

def Addspace(n):
    a=(r'[A-Z][a-z]*')
    b=re.findall(a,n)
    c=' '.join(b)
    print(c)

n=str(input())
Addspace(n)