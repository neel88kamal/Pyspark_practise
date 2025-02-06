#can we use recursion to print febonachi series upto a number
#0,1,1,2,3,5,8,13
#question is print febonachi series upto 30
num=30
final_feb_series=[]
def febonachi_series(a,b):
    if a>num:
        return 1
    print(a)
    final_feb_series.append(a)
    return febonachi_series(b,a+b)

febonachi_series(0,1)
print(final_feb_series)


#Method-2: to do same thing
def fibonacci_recursive(n, a=0, b=1):
    if a > n:
        return
    print(a, end=" ")
    fibonacci_recursive(n, b, a + b)
# Example usage
fibonacci_recursive(30)


#method-3 to do same thing
print("\n")
def fibonacci_recursive_while(n):
    a,b=0,1
    while (a<n):
        print(a,end=" ")
        a,b = b, a+b

fibonacci_recursive_while(30)