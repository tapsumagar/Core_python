#propertise  of list
#1.Two parameters are stored on one memory address which is first value as a key format and second value as a value
#2.Information shows on the basis of key and value
#3.Value accessing via key reference
#4.Key can not be duplicate and value may be duplicate
#5.Multi datatype
#6.Mutable
#7.Non indexed

dict1={'a':'hari','b':'Tapsu'}
print(type(dict1))
print(dict1)
dict2={'Nepal':'KTM','China':'Bejing', 'India':'Delhi', 'Bhutan':'Thumpu', 'boy':True, 'Girls':False, 7:9}
print(dict2)
print(dict2['Nepal'])
dict2['Nepal']='Dang'
print(dict2)
dict2.update({'Lidiya':'Tulsipur'})
print(dict2)
dict2.pop('Nepal')
print(dict2)
dict2.clear()#to delte everything.
print(dict2)











