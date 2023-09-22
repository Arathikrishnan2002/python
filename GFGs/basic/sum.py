'''
#adding two numbers

num1 = 15
num2 = 12
sum = num1+num2
print("Sum of" ,num1, "and" ,num2, "is",sum)

#adding two numbers with user input

a = input("enter the first number :")
b = input("Enter the secomnd number:")

sum = float(a)+float(b)
print("Sum is ",sum)


#with function

def add(a,b):
    return a+b
num1 = 15
num2 = 4

sum = add(num1,num2)

print("Sum is",sum)



#with add method
a = 15
b =9

import operator

sum = operator.add(a,b)

print("sum is",sum)

'''
