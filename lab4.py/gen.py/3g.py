def delenie(n):
    answer=[]
    for i in range(n):
        if (i%3==0) and (i%4==0):
            answer.append(i)
    return answer

n=int(input())
mylist=delenie(n)
print(mylist)