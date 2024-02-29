import re

def twoorthree(n):
    a=(r'ab{2,3}')
    if re.match(a,n):
        return True
    else:
        return False

n=str(input())
print(twoorthree(n))