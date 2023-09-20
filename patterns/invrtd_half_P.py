# INVERTED HALF PYRAMID USING *
n=5
for i in range(n,0,-1):
    
    for k in range(i):   
            print("*",end=" ")
    for j in range(n-i):
            print(" ",end=" ")
    print()
