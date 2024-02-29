import re

def startend(n):
    a=(r'a.*b$')
    if re.match(a,n):
        return True
    else:
        return False

n=str(input())
print(startend(n))