'''
#sum of an array
def _sum(arr):
    sum =0
    for i in arr:
        sum = sum+i
    return sum
arr = [1,2,6,8,9,3]
ans = _sum(arr)
print("sum of the array is",ans)

# using sum() 

ar = [1,2,3,4]
a = sum(ar)
print("Sum of the array  is",a)


# using enumerate

arr = [1,2,3,4,5]
s =0
for i,a in enumerate(arr):
    s = s+a
print("Sum is ", s)
'''
# using counter 
from collections import Counter

arr =  [12,3,4,3,7]
s=0
c = Counter(arr)

for key,value in c.items():
    s = s+ key*value

print("sum of the array is ",s)