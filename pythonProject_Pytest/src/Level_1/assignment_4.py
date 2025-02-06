"""Question: Find the index of the last occurrence of an element in a list.

Question: write a function that Merge two lists and sort them in ascending order.

Question: write a function that find the difference between two lists.

Question: write a function that calculate the product of all elements in the list.

Question: write a funciton that will Flatten a list of lists into a single list.

Question: write a function that Check if a list is a palindrome (reads the same forward and backward).

Question: write a function that Find the common elements between two lists.

Question: write a function that Find the common elements between two lists.

Question: write a function that Remove all occurrences of a specific element from the list.

Question: write a function that will Remove all duplicates from a list."""
from functools import reduce

#find sum of each element of a list
list_1= [1,2,3,4,5]
total_sum = sum([num for num in list_1])
print(total_sum)

#lets use reduce function
sum_reduce= reduce(lambda a,b:a+b, list_1)
print(sum_reduce)

#lets use for loop
total_value=0
for i in list_1:
    total_value+=i
print(total_value)

#we can also use recursion, i.e function calling itself but not for this use case
def sum_of_number(n):
    if n==1:
        return 1
    return n+sum_of_number(n-1)

print(sum_of_number(4))


list_test = [0,1]
print(list_test[:-3:-1])

#can we use recursion to do factorial 6 = 6*5*4*3*2*1
def fact_num(n):
    if n==1:
        return 1
    return n*fact_num(n-1)

print(fact_num(6))
