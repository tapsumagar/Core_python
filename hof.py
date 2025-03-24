"""Higher order function"""
"""
Higher finction is powerful functions. a function which take function as a argument form
Higher order function can define:
1. python builtin higher order function
2. user define higher order function
"""
 #1. python builtin higher order function
 #Map
 #Filter
 #Reduce 


"""Marks_science = [71, 50, 60, 57, 67, 44]

Marks_Nepali =[ 45, 50, 67, 70, 63, 45]

Marks_computer = [56, 67, 55, 71, 47, 49]

def avg1(a,  b, c):
    return(a+b+c)/3

x = map(avg1, Marks_computer,Marks_Nepali,Marks_science)
print(x)
print(type(x))
y= list(x)
print(y)"""

"""Marks_science = {71, 50, 60, 57, 67, 44}

Marks_Nepali ={ 45, 50, 67, 70, 63, 45}

Marks_computer = {56, 67, 55, 71, 47, 49}

def avg1(a,  b, c):
    return(a+b+c)/3

x = set(map(avg1, Marks_computer,Marks_Nepali,Marks_science))
print(x)
print(type(x))
y= list(x)
print(y)"""

Marks_science = (71, 50, 60, 57, 67, 44)

Marks_Nepali = (45, 50, 67, 70, 63, 45)

Marks_computer = (56, 67, 55, 71, 47, 49)

def avg1(a,  b, c):
    return(a+b+c)/3

x =tuple(map(avg1, Marks_computer,Marks_Nepali,Marks_science))
print(x)
print(type(x))
y= list(x)
print(y)



