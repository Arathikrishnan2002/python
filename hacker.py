"""
the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
input ABCDCDC
      CDC
output 2 
"""
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if(string[i:i+len(sub_string)]== sub_string):
            count +=1
        
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


"""You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""
if __name__ == '__main__':
    s = input()
    
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False
    
    for i in s:
    
        if i.isalnum() == True:
            isalnum = True
    
        if i.isalpha() == True:
            isalpha = True
    
        if i.isdigit() == True:
            isdigit = True
    
    
        if i.islower() == True:
            islower = True
    
        if i.isupper() == True:
            isupper = True
    
    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)
    
