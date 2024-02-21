import math
def mnogougolnik(a,k):
    s=((k*a**2)/4)
    t=((1/(math.tan(180/k))))
    e=s*t
    return e 

k=int(input("Input number of sides:"))
a=int(input("Input the length of a side:"))
print("The area of the polygon is:",mnogougolnik(a,k))

