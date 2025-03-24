"""
Reduce:
-Reduce use iterative technique
-It takes a large collection and merging iterative(one by one)
    on one single output according to give logic
    -It used compulsory library package (from functools import reduce)
    Syntax: variable = (function, collection)
    
"""
"""WAP to calculate sum of list"""
from functools import reduce
list_num=[1, 2, 3,4,5]
print(reduce(lambda x, y:x+y,list_num))