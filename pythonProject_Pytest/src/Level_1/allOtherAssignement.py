# Calculate sum of all numbers from 1 to a given number
# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)
#
total_sum=0
sumupto = int(input("enter an integer upto which you need to calculater sum upto: "))
for i in range(1,sumupto+1):
    total_sum+=i

print(f"total sum is {total_sum}")

#Display Fibonacci series up to 10 terms.
#For example, 0, 1, 1, 2, 3, 5, 8, 13, 21.
# The next number in this series is 13 + 21 = 34. febonachi series
list1=[0,1]
sum1=0
for i in range(1,10):
    a,b= list1[-1:-3:-1]
    # print(a,b)
    sum1 = a+b
    list1.append(sum1)
    if len(list1)>10:
        break
print(list1)

'''Find the sum of the series up to n terms
               Write a program to calculate the sum of series up to n terms.
               For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
'''
sum=0
series='2'
for i in range(1,6):
    sum+=int(series*i)
    print(series*i,end="+")
print("\n sum= ",sum)

