"""
onject-orinted programming
In python, Everything are objects.Whatever,coding technique may be procedural method.
Because object method as treats the programming behind the process,
OOP is used to implement and store real word entity,
OOP ca create own class as like Data structure that means OOP technique is
creating own datatype where you want store data.
class is used to represent capital letter starts real word entity
class name
"""
"""
   Syntax:
   class <class_name>(parent classes(optional)):
   #description of class'attributes (data which stores few data)
   behavior(behavior is used to modify attributes/function /method)
"""
print("---------Start Attributes---------  ")

class Teacher:
    age = 26
    name = 'Tapsu Magar'

object1 = Teacher()
print(type(object1))
print(object1.age)

object2 = Teacher()
print(type(object1))
print(object1.age)

object2 = Teacher()
print(object2.name)
object2.name='Dikhsya Gharti' #creates different memory address and stores the new data too
print(object2.name)
print(object1.name)

class Student:    
    age = 20     #attributes
    name = 'Tapsila P Magar'  #attributes
    def inc_age(self):  #behaviour /function
        self.age +=1  # self is pointer/function

object3 = Student()
object3.age= 24
object3.inc_age()
print(object3.age)

object3.inc_age()
print(object3.age)

object4 = Student()
object4.age=20
object4.inc_age()
print(object4.age)


"""
Here, inc_age() function represents as behaviour in these class
and self-pointer passed in that function.
self is pointer like "this pointer" in java
A class has many objects and multiple objects are using same method/behaviour/function
this condition we can not define which object called the function then we can't pass argument
of particular object. so, we are solve problem by passing sef_pointer in the function
as a argument form. When self_ponter is passed in a function then self_pointer decide
automatically which objects of argument is passed in the function and finally,the function
can use argument according to calling object.
"""

#So, when objects called inc_age(self) function of class student and in this situation,
#Self automatically invoked age_argument for object5 in the inc_age function.

"""
In class, To change or update all attributes dynamically via using constructor
To accessing all attributes from anywhere
Contructor is also a behavior. constructor is self automatically called or run during the objects crested in programs

"""
"""class Learn:
    name = 'Ramesh Magar'

    def __init__(self):
        print('This function is automatically called during object is created')


object7 = Learn()
object8 = Learn()"""


"""Here, __init__ constructor function is automatic run two time because
Learn class has two objects (objects1 and objects2).
Note: in python, constructor is automatically called(run) during class of objects are
creating state in the class
"""

class Database1:
    def __init__(self, name, age, salary):
        self.arg1 = name
        self.arg2 = age
        self.arg3 = salary

        print(self.arg1 + ' is created') #plus for strings
        print(self.arg2,  ' old year') #coma for integers
        print(self.arg3,  ' salary income')

data_ob1 = Database1('Mina', 67, 6000)