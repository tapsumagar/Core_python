"""Frozenset"""
"""
append non-mutable propertise in all Basic datatype content and collection data structure
syntax: Variable = frozenset(iterable)
frozenset is key point for non-mutable
"""
set1={1, 2, 3, 4, 6}
print(set1)
set2=frozenset(set1)
print(set2)
set1.add(10)
print(set1)
set2.add(12)
print(set2)