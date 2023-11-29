# deep copy and shallow copy in python

#Syntax of Python Deepcopy
#Syntax: copy.deepcopy(x)


#A deep copy creates a new compound object before inserting copies of the items
#found in the original into it in a recursive manner.
#It means first constructing a new collection object and then recursively
#populating it with copies of the child objects found in the original.
#In the case of deep copy, a copy of the object is copied into another object.
#It means that any changes made to a copy of the object do not reflect in the original object. 

#A shallow copy creates a new compound object and then references the objects
#contained in the original within it, which means it constructs a new collection
#object and then populates it with references to the child objects found in the original. The copying process does not recurse and therefore won’t create copies of the child objects themselves. In the case of shallow copy, a reference of an object is copied into another object. It means that any changes made to a copy of an object do reflect in the original object.
#In python, this is implemented using the “copy()” function. 
#1. SHALLOW COPY
import copy

old_list=[[1,2,3],[5,6,7],[8,9,0]]
new_list=copy.copy(old_list)
new_list[0]=['a','b','c']
print("Old list:",old_list)
print("New list:",new_list)



#OUTPUT:
#Old list: [[1, 2, 3], [5, 6, 7], [8, 9, 0]]
#New list: [['a', 'b', 'c'], [5, 6, 7], [8, 9, 0]]

# but when we are changing the element changes in both new_list and old_list are made

#import copy
#old_list=[[1,2,3],[5,6,7],[8,9,0]]
# new_list=copy.copy(old_list)
#new_list[0][2]=['d']
# print("Old list:",old_list)
#print("New list:",new_list)

# Old list: [[1, 2, ['d']], [5, 6, 7], [8, 9, 0]]
# New list: [[1, 2, ['d']], [5, 6, 7], [8, 9, 0]]

# For not changing the element in the old list we will use deep copy

import copy
old_list=[[1,2,3],[5,6,7],[8,9,0]]
new_list=copy.deepcopy(old_list)
new_list[0][2]=['d']
print("Old list:",old_list)
print("New list:",new_list)

#Old list: [[1, 2, 3], [5, 6, 7], [8, 9, 0]]
# New list: [[1, 2, ['d']], [5, 6, 7], [8, 9, 0]]
