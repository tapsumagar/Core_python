Marks_science = (71, 50, 60, 57, 67, 44)

Marks_Nepali = (45, 50, 67, 70, 63, 45)

Marks_computer = (56, 67, 55, 71, 47, 49)

def avg1(a,  b, c):
    return(a+b+c)/3

x =tuple(map(avg1, Marks_computer,Marks_Nepali,Marks_science))
print(x)
y=list(map(lambda i, j, k:(i+j+k)/3,Marks_computer,Marks_Nepali,Marks_science))
print(y)

g=[3, 4, 6, 7]
w=[1, 7, 2, 8]
import math
c= list(map(lambda a, b:math.sqrt(a**2+b**2),g,w))
print(c)



