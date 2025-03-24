"""
list collection and data structure 
syntax:
       variable = [value 0, value 1, ..., value n]
       list()  ->constructor

 propertise of list 
 1. Index and Slice
 2.Multible (delete, update,....)
 3.Multi-datatype
 4.Item Dublications      

"""
# person_name = ['Hari', 'Shyam',1, 1.1, True]
# print(type(person_name))
# amc=['rollnu', 'name', 'address', 1, False, True, 1]
# print(amc)
# #index
# print(amc[2])

# student_name = ['Sita' 'Rukum', 10, 'Hari', '11', 'false', True, 1]
# print(student_name[0:8:2])
# print(student_name)

# amc.append ('Tapsu')
# print(amc)
# amc.extend(['Mina', 'Dina', 'Rima'])
# print(amc)
# print(amc.count(1))
# amc.remove(1)
# print(amc)
# amc.pop(3)
# amc.pop()
# print(amc)
# amc.reverse()
# print(amc)

dang=["Barakune","Dharapani","Lakhanpark","Ganeshpark","Karjaya"]

Num=[78, 34, 45, 67, 70, 60]
Num.sort()
print(Num)
dang.sort()
print(dang)
Num.sort(reverse=True)
print(Num)
Num[1]='Tero'
print(Num)