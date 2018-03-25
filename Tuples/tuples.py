# Tuple is a sequence of immutable python objects
# Unlike lists, tuples can not be changed and are
# enclosed in parenthesis
tuple1 = ("physics", "biology", 1995, True)
tuple2 = "a", "b", "c", "d"
tuple3 = (1,2,3,4,5)
tuple4 = () # empty tuple
tuple5 = (4,) # single value tuple should have a comma at the end

# Accessing values in a tuple
print "Accessing values in a tuple"
print tuple1[3]
print tuple2[0]
print tuple3[1:3]

# updating values in a tuple

		# NOT OPERATIONAL

# removing tuple
# not operation on individual element but the entire tuple
print "Deleting a whole tuple!!"
del tuple4
print "After deleting tuple4"
print tuple4

# NB
# Tuples include all list operation such as
# membership
# repetition
# concatenation and
# iteration