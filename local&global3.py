####  LOCAL AND GLOBAL VARIABLES

>>>>> In Python when you want to use the same variable for rest of your program or module you declare it a global variable.
 
>>>>> While if you want to use the variable in a specific function or method, you use a local variable.

# Declare a variable and initialize it
f = 101   # global define
print f   # o/p is '101'

# Global vs. local variables in functions

def Function():
# global f
    f = 'I am learning Python'
    print f # o/p is 'I am learning python'.
Function()
print f    # o/p is '101'.


#######

f = 101;
print f  # o/p is '101'.

# Global vs.local variables in functions

def Function():
  global f
print f     # o/p is '101'.
f = "changing global variable"

Function()
print f  # o/p is 'changing global variable'.


### delete variable using delete function.
f = 11;
print(f)
del f
print(f)
