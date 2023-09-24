
'''
# maximum

def max(a,b):
    if a>=b:
        return a
    else:
        return b
        
a=2
b=3
print(max(a,b))

# using max function

a = 9
b =7

result = max(a,b)
print(result)


# using ternary operator

a = 15
b =7

print(a if a>=b else b)

# list comprehension

a = 6
b=21

x = [ a if a>=b else b]
print(x)


# using sort() method

a =96
b =92

x = [a,b]
x.sort()
print(x)
print(x[-1])

'''
