What is Tuple..?

>> A tuple is just like a list of a sequence of immutable python objects. 
>> The difference between list and tuple is that list are declared in square brackets and can be changed while tuple is declared in parentheses and cannot be changed.

>> tuple allows you to use many built-in functions like all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc.

>> Tuples are immutable and cannot be deleted, but deleting tuple entirely is possible by using the keyword "del."

tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida')
tup2 = (1,2,3,4,5,6,7)
print  tup1[0]
print  tup2[1:4]

#Packing and Unpacking
x = ("amit", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print company
print emp
print profile

#Comparing tuples
#case 1
a=(5,6)
b=(1,4)
if (a>b):print "a is bigger"
else: print "b is bigger"

#case 2
a=(5,4)
b=(5,6)
if (a>b):print "a is bigger"
else: print "b is bigger"

a=(5,6)
b=(6,4)
if (a>b):print "a is bigger"
else: print "b is bigger"

#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.items()
print b 

#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print x[2:4]

