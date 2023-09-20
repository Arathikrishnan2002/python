# half pyrmid pattern using *
n=5
for i in range(1,n+1):
    
    for k in range(i):   
            print("*",end=" ")
    for j in range(n-i):
            print(" ",end=" ")
    print()
