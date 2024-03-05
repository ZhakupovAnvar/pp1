def camel_to_snake(n):
    s = ""
    for char in n:
        if(char.isupper()):
            s += '_' + char.lower()
        else:
            s += char
    if s.startswith('_'):
        s = s[1:]
    return s
n=str(input())
print(camel_to_snake(n))