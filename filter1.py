"""
filter
syntax:collection_casting(filter(function(boolean), collection(single)))

-using function must be a return boolean type result like True or False otherwise wrong
-we can pass only a single collection in filters
-It is used in the list and tuple or operate and casting beacause it has indexing features
"""
"""WAP to show only even number"""

#num is default input argument
#num2 is optional input 

def is_even(num1, num2=0):
    if num1 % 2 ==0:
        return True
    else:
        return False
    

list1 = [2, 3, 6, 7, 12, 13]
output1 = list(filter(is_even,list1))
print(output1)

def is_odd(num1, num2=0):
    if num1 % 2 !=0:
        return True
    else:
        return False
    

list1 = [2, 3, 6, 7, 12, 13]
output1 = list(filter(is_odd,list1))
print(output1)


y = list(filter(lambda num1: num1 % 2 != 0, list1))
print(y)




Marks_science = (71, 50, 60, 57, 67, 44)

Marks_Nepali = (45, 50, 67, 70, 63, 45)

Marks_computer = (56, 67, 55, 71, 47, 49)


per = list(map(lambda x, y, z: (x+y+z)/3, Marks_computer,Marks_Nepali,Marks_science))
print(per)

pass_result = list(filter(lambda ob_per:ob_per>=60,per))
print(pass_result)
inone = list(filter(lambda ob_per:ob_per>=60, list(map(lambda x, y, z:(x+y+z)/3,Marks_computer,Marks_Nepali,Marks_science))))
print(inone)


