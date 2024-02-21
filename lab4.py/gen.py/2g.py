def evens(n):
    answer=[]
    for i in range(n):
        if i % 2 == 0:
            answer.append(i)
    return answer

n = int(input())
mylist = evens(n)
print(mylist)