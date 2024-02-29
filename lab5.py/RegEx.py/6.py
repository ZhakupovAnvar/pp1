import re

def replacing(n):
    a=(r'[ ,.]')
    b=re.sub(a,':',n)
    print(b)

n=str(input())
replacing(n)
