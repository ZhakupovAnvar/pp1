import time
import math

def my(num, milisec):
    time.sleep(milisec / 1000) 
    result = math.sqrt(num)
    return result

num = int(input())
milisec = int(input())
answer = my(num, milisec)
print(f"Square root of {num} after {milisec} miliseconds is", answer)