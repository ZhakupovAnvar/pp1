def delenie(n):
    for i in range(n):
        if (i%3==0) and (i%4==0):
            yield i
    

n=int(input())
mylist=[i for i in delenie(n)]
print(mylist)