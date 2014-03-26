##Square root
num = float(input('get int: '))
guess = num/2
delta = 0.01
dif = abs(num - guess*guess)
i=0
while dif>delta:
    guess = (guess + num/guess)/2
    dif = abs(num - guess*guess)
    i=i+1
import math    
math = math.sqrt(num)
print(num,guess,math,i)

