n=5

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(1, n - i + 1):
        print(" ", end=" ")
        
        # Print increasing numbers
    for k in range(i, 0, -1):
        print(k, end=" ")
        
        # Print decreasing numbers
    for l in range(2, i + 1):
        print(l, end=" ")
        
        # Move to the next line
    print()