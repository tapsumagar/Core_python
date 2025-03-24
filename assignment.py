#Write a python functionto find the max of 3 number.
"""a=int(input("Enter the first number="))
b=int(input("Enter the second number="))
c=int(input("Enter the third number="))

def find_max(a, b, c):
    return max(a, b, c)

print("The maximum number is:", find_max(a,b,c))"""

#Write a python function to sum all the number in the list.(8,2,3,0,7)
"""def add_data():
    list7 = [8, 7, 5, 7, 8]
    total = 0
    for num in list7:
        total = total + num
    return total

j=add_data()
print('The sum {} of given list'.format(j))"""

#Write a python function to calculate the factorial of a number (a non-negative integer)
"""def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        return fact
n=int(input("Enter positive number 'N': "))
f=factorial(n)
print('facttorial is: ',f)"""


#Write a python functionto find the max of 3 number.
"""x=int(input("Enter the first number="))
y=int(input("Enter the second number="))
Z=int(input("Enter the third number="))

def max_find(a, b,c):
    if a>b and a>c:
        print('The first number {} is largest number'. format(a))
    elif b>a and b>c:
         print('The second number {} is largest number'. format(b))
    else:
        print('The third number {} is largest number'. format(c))
    return max_find

d=max_find(x,y,Z)
print(d)"""

#Define a function is_even that will take a number x as input . If x is even then return True otherwise return false.
n=int(input("Enter the number"))

"""def is_even(n):
    if n%2 == 0:
        print('True')
    else:
        print('false')
    return is_even

e=is_even(n)
print(e)"""

#Write a function called digit_sum that can take any number of integer arguments takes returns the sum of all that number's digits.
#Write a python function that accepts a string and calculates the number of upper case letters and lower case letters . (simple string:The quick brown fox.)
def count_case_letters(input_strings):
    upper_case_count = 0
    lower_case_count = 0

    for char in input_strings:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
    return upper_case_count, lower_case_count

use_input = input("Enter a string")
upper_count, lower_count = count_case_letters(use_input)
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")

#WAP to check whether a string is palindrome or not.
#WAP a program that returns a list that returns only the elements that are common before list.
