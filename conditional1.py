a=int(input('Enter the first number'))
b=int(input('Enter second number'))
# sum1 = a + b
# print(sum1)
# if a>b:
#     print('a is greater number')
# else:
#     print('b is greater')

if a==0:
    print('This is null')
    print('This is yes part of condition')
elif a % 2==0:
    print('This is even number')
else:
    print('This number is odd')

    #nested if
if b==0:
    print('This is null number')
    if b % 2==0:
      print('This even number')
    else:
        print('This is odd number')
else:
    print('This las if off')


if a %2==0 and a %4==0:
    print('This number is exactly divisable by 2 and 4')
else:
    print('This is not di....')


