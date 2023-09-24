'''

# factorial of a number using iterative approach
def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else :
        fact =1
            
        while n>1:
            fact = fact*n
            n-=1
        return fact
num=5
print("factorial of " ,num,"is ",factorial(num))


#using recursive approach / ternary operator

def fact(n):
    return 1 if(n==0) or (n==1) else n*fact(n-1)
    
num =5
print("factorial of " ,num ,"is",fact(num))


# using for loop

def fact(n):
   
    fact = 1
    for i in range(2,n+1):
        
        fact = fact*i
    return fact
    
num = 5
print("factorial is ",fact(num))



# using built in function

import math
def fact(n):
    return math.factorial(n)
num = 5
print("factorial is",fact(num))
'''


