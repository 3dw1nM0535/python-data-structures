"""We will kick this section with arrays.
Most Data structures make use of arrays to implement
their algorithms. The following are important terms to understand
1) Element => each item stored in the array is an element
2) Index => the position occupied by an element in the array

Basic array operations include:

1) Traverse => print all array element one-by-one
2) Insertion => add an element at the given index
3) Deletion => remove an element at the given index
4) Update => update an element at the given index
5) Search => search an element using the given index or value
"""

# Array is python are created by importing the array module
# to our python program

"""
from array import *
arrayName =array(typecode, [Initializers]);
"""

# where typecode define the type of array values our array will hold
from array import *
arr = array("i", [10, 20, 30, 40, 50])
# "i" defines the type of our array value to be integers
# print each element of our array
for i in arr:
	print i

# accessing array element
print "Element => ", arr[0]
print "Element => ", arr[3]
print "Element => ", arr[2]

# inserting operation
arr.insert(1, 60) # inserts at position 1
# Traverse to see the new array
print "Array after inserting new element"
for i in arr:
	print i

# delete operation
arr.remove(40);
# Traverse the array to see the new array
print "Array after removing element"
for i in arr:
	print i

# search operation
# if element is not in the array, python will return an error,
# else it will return the index of the element if found in the array
print "Found element at"
print arr.index(50);

# update operation
# we simply reassign a new value to the desired index we want to update
print "Assigning new value to array"
arr[3] = 100
# Traverse the array to see the new array
for i in arr:
	print i
