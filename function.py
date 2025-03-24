"""function"""
#A function are something that takes n number input(argument)and then transfer into a output
"""
f(x) = x+1
propertise of function
1. It takes 0 to more input(args/parameters in java,C)
2. It returns 0 to values
  but other program c, java return a value at one time execution
  syntax:

    def <function_name> (args1, args2, .., aregs n):
      ->description
      ->logic (simple/complex)
      ->return output (optional)

 Note: Insert 2 blank line after and before of functions
"""

def name():
    #this is simple python function
    print('hello')

# name() # function call without argument

# for i in range(10):
#     name()
# x= int(input('Enter the first Number='))
# y= int(input('Enter the second number='))

# def add1(a,b):
#     adding = a+b #logic
#     print(adding)

# c=add1(x,y)
# print(c)
"""
p= int(input('Enter the first time='))
q= int(input('Enter the second principle='))
r= int(input('Enter the third rate='))

def SI(a,b,c):
    SI =a*b*c/100
    return SI

Simple_Interest =SI(p,q,r)
print(Simple_Interest)
"""

x= int(input('Enter the first Number='))
y= int(input('Enter the second number='))

def arthemetic(a,b):
    adding = a+b
    subtract1= a+b
    multi= a*b
    divide1=a/b
    return adding, subtract1, multi, divide1

c=arthemetic(x,y)
print(c)
h, i, j, k  = arthemetic(x,y)
print('This varia unpacking and store adding at=', h)
print('This varia unpacking and store adding at=', i)
print('This varia unpacking and store adding at=', j)
print('This varia unpacking and store adding at=', k)
print(h)
print(i)
print(j)
print(k)



    

