#without using power function

n =8208
s=n
b = len(str(n))
sum=0
while n!=0:
    r = n%10
    sum = sum+(r**b)
    n = n//10
if s==sum:
    print(s,"is an Amstrong number")
else:
    print(s,"is not an Amstrong number")
    
