#1 Required argument
def sum1(x, y):
    add= x+y
    return add

c = sum1(1,2)
print(c)

#default argument
def sum1(x=1, y=2):
    add=  x+y
    return add

c = sum1()
print(c)

#some argument are default and some required
def sum1(x, y=2):
    add=x+y
    return add

c = sum1(2)
print(c)

#argument are define at calling
def sum1(x, y):
    add= x+y
    return add

c = sum1(y=2,x=5)
print(c)


def listdisplay(*input1):
    list1= list(input1)
    tuple1= tuple(input1)
    set1=set(input1)
    return list1, tuple1, set1

c=listdisplay(1, 2, 3, 4, 5, 6, 7)
print(c)

def dicr1(**input2):
    return input2

g= dicr1(c1=1,c2=12,c3=23)
print(g)