# set1={1,2,3,4,5,6,7,'amc',1,True,'dang', 'amc'}
# print(type(set1))
# print(set1)
# set1.add('dino')
# print(set1)
# set1.remove(2)
# set1.pop()
# print(set1)
# set1.discard('Rukum')
# set1.discard('dino')
# print(set1)

set1={1,2,3,4,5,6,7,'amc',1,True,'dang', 'amc'}
set2={9,10,12,1}
print(type(set1))
print(set1)
first=['data1','data2','data3']
f=set(first)
second=['ameb','bmeb','cmeb']
s=set(second)
b=set1.union(set2)
print(b)
print(f.union(s))

third=(14,16,17)
t=set(third)
fourth=('s1','s2','s3')
f=set(fourth)
h=set(fourth)
print(t.union(h))
print(t.intersection(h))
print(t.intersection(h))
print(t.difference(h))
print(t|h)
print(t&h)
