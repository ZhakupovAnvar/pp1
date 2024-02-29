import re

def dalshe(n):
    a=(r'ab*')
    if re.match(a,n):
        return True
    else:
        return False

n=str(input())
print(dalshe(n))