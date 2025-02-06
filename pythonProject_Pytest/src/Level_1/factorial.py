#Python program to find the factorial of a number.
#factorial of 6 is 6*5*4*3*2*1 = 720
from sympy import factorial

num = int(input("enter an integer less than 10: "))
factorial = 1
while (num>1):
     factorial= factorial*num
     num-=1
print(factorial)
