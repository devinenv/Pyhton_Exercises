""" program to print digits and
    its operations
"""

# Implement the helper functions here

def perform_check(num):
    if num > 9 and num1 < 100:
        print("entered number is two digit number:", num)
        
    elif num > 99 and num < 1000:
        print("entered number is three digit number:", num)
        
    elif num > 0 and num < 10:
        print("entered number is single digit number:", num)
        
    else:
        print("entered number is nor a single/double/tripple digit number:", num)
    return num
    

def get_number():
    num = int(input("Enter any number:"))
    return num
   
# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)


