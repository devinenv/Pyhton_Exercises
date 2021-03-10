""" program to print digits and
    its operations
"""

# Implement the helper functions here

def perform_check(num):
    if num > 9 and num < 100:
        print("entered number is two digit number:", num)
        num = num ** 5
        num = num % 10
        print("number in unit's place:",num)
        
    elif num > 99 and num < 1000:
        print("entered number is three digit number:", num)
        new_num = int(input("enter another number:"))
        num1 = num + new_number
        num = num1 % 10
        print("number in unit's place:",num)

    elif num > 0 and num < 10:
        print("entered number is single digit number:", num)
        num = num + 7
        num= num % 10
        print("number in unit's place:",num)
        
    else:
        print("entered number is nor a single/double/tripple digit number:", num)
    return num
    

def get_number():
    num = int(input("Enter any number:"))
    return num
   
# Main starts from here
num1 = get_number()
perform_check(num1)


