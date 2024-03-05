import re

def snakeToCamel(n):
    a=n.split('_')
    CamelString= a[0]
    for char in a[1:]:
        CamelString += char.capitalize()
    return CamelString

n=str(input())
print(snakeToCamel(n))