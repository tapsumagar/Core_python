""" Generator"""

""" Generator is used to create a new collection with the help of existing collection
 Application of generator

"""

"""
compile time : if programming is execute then program is compiled by compiler before run time and run all 
related task with assign memory address and it can be take memory space
for eg: num = [1,4,5,7,8,12,56,76,89,90,95]
print(num)
here, list num is created in compiled time and memory space is consumed at the same time 

2. runtime: In programing, some block of code is compiled by compiler at the runtime after whole compiler
            that mean's programming create or released all task and assign memory space at runtime

            
comprehension is also called laZy evaluater it is compiled by compiler at the runtime after whole compiler
and consume memory at same runtime
   print([logi loop condition])
"""

#WAP to replace even number with 'even' and odd number with 'odd'
#hint : list_name=[2,3,6,8,14,17,20,7,9,4]
"""list_name =[2,3,6,8,14,17,20,7,9,4]
h = ['even' if list_data % 2 ==0 else 'odd' for list_data in list_name]
print(h)
print(type(h))

tuple_name =(2,3,6,8,14,17,20,7,9,4)
s = ['even' if tuple_data % 2 ==0 else 'odd' for tuple_data in tuple_name]
print(s)
print(type(s))

set_name ={2,3,6,8,14,17,20,7,9,4}
t = ['even' if set_data % 2 ==0 else 'odd' for set_data in set_name]
print(t)
print(type(t))
"""


#WAP to find if 1 comes in list then yes/ if 2 comes in list then no/ otherwise idle
list_name1 = [1, 0, 3, 2, 5, 7, 1]
y= ['yes' if data3== 1 else 'No' if data3==2 else 'idele' for data3 in list_name1]
print(y)

tuple_name1 = (1, 0, 3, 2, 5, 7, 1)
x= ['yes' if data3== 1 else 'No' if data3==2 else 'idele' for data3 in tuple_name1]
print(x)

set_name1 ={ 1, 0, 3, 2, 5, 7, 1}
Z= ['yes' if data3==1 else 'No' if data3==2 else 'idele' for data3 in set_name1]
print(Z)

def ch_even_odd(num):
    #this solution by function
   if (num % 2 ==0):
        return 'even'
   else:
        return 'odd'

p= [ch_even_odd(num) for num in list_name1]
print(p)


def ch_yes_No(num):
   if (num % 2 ==1):
       return 'yes'
   elif (num % 2 ==2):
       return 'No'
   else:
      return 'idle'

   
t= [ch_yes_No(num) for num in list_name1]
print(t)

def ch_yes_No(num):
   if (num% 2 ==1):
       return 'yes'
   elif (num% 2 ==1):
       return 'No'
   else:
      return 'idle'

   
x= [ch_yes_No(num) for num in tuple_name1]
print(x)


    
    