# Lists have the same concept behind array.
# The super advantage of using list over 
# array is that with lists, they can hold any
# data type not just the same data type elements
# Lists can be sliced, concatenated and so on

list1 = ["physics", 1995, True,]
list2 = [1,2,3,4,5]

print "Original list 1"
for i in list1:
	print i

print "Original list 2"
for i in list2:
	print i

# Accessing values in a list
print "Accessing list element"
print list1[0] # same concept just like arrays
print list2[2]

# Updating elements in the list is quite as arrays
list1[0] = 10
list2[3] = "Physics"
# Traverse the list to see the new list
print "Updated List 1"
for i in list1:
	print i

print "Updated List 2"
for i in list2:
	print i

# delete operation
# you can use remove() if you don't know which element to delete
# or del if you know which element to delete
print "List 1 after removing element"
list1.remove(True)
for i in list1:
	print i

print "List 2 after removing element"
list2.remove("Physics")
for i in list2:
	print i

print "Length of list1"
print len(list1)

print "Length of list2"
print len(list2)

# concatenation
print "Concatenating the list1 with list2"
print list1 + list2

# Repetition
print "Repeat list1 4 times"
print list1 * 4
print "Repeat list2 4 times"
print list2 * 4

# membership
print "Check if value exist in list1"
print 1995 in list1

print "Check if value exist in list2"
print 5 in list2