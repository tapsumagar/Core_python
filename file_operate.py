"""
1. file is actual data of any things
some file type are: .txt, csv, .log, .json, .xml, etc
syntax: open(location,mode) -> file pointer
modes are: 1)w mode for write only
           2)r mode for read only
           3)a mode for append as well as update content
Advance modes are: 4) wb mode for write binary
                   5) rb mode for read binary
                   6) x mode for write only
                   7) rw mode for
"""
#write mode
"""
1. overwrite the content, if already this name's file is exist in machine
2. if file doesn't exist it will create new one.
"""
csb=open('computer.txt','w')
csb.write('This is the first practice')
csb.close()

#advance form
with open('data.txt','w')as file_pointer:
    file_pointer.write('This is the first line \n')
    file_pointer.write('This third line content')
    file_pointer.writelines(('First line appear\n','second line appear\n','Third line appear'))

#read mode

with open('data.txt', 'r')as f:
      tapsu=f.read()
print(tapsu)

#seek function
with open('Rima.txt','w')as g:
     g.write('This is the data for seek function')

with open('Rima.txt','r')as h:
     home1 = h.read()
     print(home1)
     j = h.seek(4)
     print(j)

#append mode
with open('Rima.txt', 'a')as r:
     r. write('\nThis is append content')
     r.write('\nThis second append data')

import pickle 

# list_number=[1, 2, 3, 4, 5, 7]
# with open('binod.pkl', 'wb')as po:
#      pickle.dump(list_number,po)

# with open('binod.pkl','wb')as po:
#      pickle.dump(list_number,po)

# with open('binod.pkl','rb')as lock:
#      h= pickle.load(lock)
#      print(h)
#      print(type(h))

# set_number={1, 2, 3, 4, 5, 7}
# with open('binod.pkl', 'wb')as po:
#      pickle.dump(set_number,po)

# with open('binod.pkl','rb')as lock:
#      h= pickle.load(lock)
#      print(h)
#      print(type(h))


dict_number={'gita':'dikhsya','tapsu':True}
with open('binod.pkl', 'wb')as po: #po vaneko file pointer ho
      pickle.dump(dict_number,po) # pickle ra dump vaneko function ho

with open('binod.pkl','rb')as lock:#lock vaneko file pomter ho
      h= pickle.load(lock) # h vaneko list ho
      print(h)
      print(type(h))



import json
dict_data = {'Nepal':'KTM', 'Bhutan':'Thmpu', 'china':'Bejing'}

with open('datafile.txt','w') as opps:
     opps.write(json.dumps(dict_data))

with open('Bina.txt', 'w')as opps1:
     opps1.write(str(dict_data))


db = {}
b = pickle.dumps(db)
c = pickle.loads(b)
print(c)



#onlly write mode 
#it can create duplicate file in same place in your machine
#x/write mode le ekchoti marta kam garxa
"""hi = open('Tapsu.txt', 'x')
hi.write('This is the only write mode and it can not create duplicate file')
hi.close()

"""
import os
if os.path.exists("Bina.txt"):
     os.remove("Bina.txt")
     print("File deleted")
else:
     print("file doesn't exist")

# import os
# if os.path.exists("data.txt"):
#    os.rename('data.txt','tapsu_p.txt')
#    print("file renamed")
# else:
#      print("file doesn't exist")

#seek function
tom = open('tapsu','w')
tom.write('simultanausly perform like human')
tom.close()

tom = open('tapsu', 'r')
before1 = tom.read()
print(tom)

tom.seek(3)
after1=tom.read()
print(after1)