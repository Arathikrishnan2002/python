'''

# maximum element in an array

def largest(arr,n):
    
    max = arr[0]
    n = len(arr)
    for i in range(0,n-1):
        if arr[i] > max:
            max = arr[i]
    return max

arr =[1,23,65,17,75,2]
n = len(arr)
ans = largest(arr,n)
print("Maximum elemnt of the array is ",ans)

# using max()

arr = [ 12,6,3,98,71]
for i in arr:
    ans = max(arr)

print("Maximum elemnt of the array is ",ans)

# using sort()

def largest(arr, n):
 
    arr.sort()
    return arr[n-1]

arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

'''