
# getting input from terminal
print "How old are you?",
age = raw_input()

# use on files:
close, read, readline, truncate (empties the file), write("stuff")

if A:
    #bla
elif B:
    #bla 2
else:
    #blabla

x = 10
9 < x < 11 # this will evaluate.
# or:
x in range(1,10)  

fruit = ['a','b','c']
for f in fruit:
    print "bla bla %s" % fruit 
    
exit(0) % exits with no error. exit(1) exits with error

for i in range(len(a)):
or:
for i in enumerate(a):
range(10) % gives list of [0, 1, ... 9]

# try except finally grammar:
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"
 
dir() # to see what's in workspace
who # gives a list of variables in ipython

# continue:
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter
# prints P, y, t, o, n   
  
# useful functions
type(x) # gives the class of x
who # lists what's in the workspace
dir() # more holistic list

# generator functions:
# define a generator function by having a 'yield' for the returns.
def simple_generator_function():
    yield 1
	yield 2
	
for value in simple_generator_function():
    print(value)

#ipython:
%paste # (to paste code)
%run # ( to run script)

#or!:
out1 = next(simple_generator_function) # yields 1
out2 = next(simple_generator_function) # yields 2
out3 = next(simple_generator_function) # gives error, since the iterable is done.

# sending vals to generators
def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number # here, number (on the left) will be taken in as val if use send(number)
        number += 1

# closures: **return** a function that does something as defined by the outer function
def add_number(num):
        def adder(number):
            #'adder is a closure'
            return num + number
        return adder

# decorators:
def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Before call")
            result = func(*args, **kwargs)
            print("After call")
            return result
        return wrapper

@my_decorator
    def add(a, b):
        #"Our add function"
        return a + b
        
# join:
'-'.join(('a','b','c','d'))

	
# commands:
for	# Loop over a collection of things.	for X in Y: pass
if	# If condition.	if: X; elif: Y; else: J
and	# % Logical and.	True and False == False
break # 	Stop this loop right now.	while True: break
def	#Define a function.	def X(): pass
elif #	Else if condition.	if: X; elif: Y; else: J
else #	Else condition.	if: X; elif: Y; else: J
exec #	Run a string as Python.	exec 'print "hello"'
from #	Importing specific parts of a module.	import X from Y
global # 	Declare that you want a global variable.	global X
import #	Import a module into this one to use.	import os
in #	Part of for-loops. Also a test of X in Y.	for X in Y: pass also 1 in [1] == True
is #	tests if the names point to the same object. a is a == True, but 1000 is 10**3 == False (since they do not point to the same object).
not #	Logical not.	not True == False
or #	Logical or.	True or False == True
pass #	This block is empty.	def empty(): pass
print #	Print this string.	print 'this string'
return #	Exit the function with a return value.	def X(): return Y
try #	Try this block, and if exception, go to except.	try: pass % try: block, except ErrorType as e: "print something about error"
raise #	Raise an exception when things go wrong.	raise ValueError("No")
while #	While loop.	while X: pass
assert #	Assert (ensure) that something is true.	assert False, "Error!"
continue #	Don't process more of the loop, do it again.	while True: continue
del #	Delete from dictionary.	del X[Y]
except #	If an exception happens, do this.	except ValueError, e: print e
finally #	Exceptions or not, finally do this no matter what.	finally: pass

as #	% Part of the with-as statement.	with X as Y: pass (also except as? others?)
with #	With an expression as a variable do.	with X as Y: pass
lambda :## Create a short anonymous function.	s = lambda y: y ** y; s(3)

# need to look up:
yield #	Pause here and return to caller.	def X(): yield Y; X().next() # generators!!
# generators 

class #	Define a class.	class Person(object)


# look up this for in if syntax/grammar!!
def get_primes(input_list):
    return (element for element in input_list if is_prime(element))
	
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
<<<<<<< Local Changes
#look up iterables (what is iterable? generators, enumerate objects)..


# classes:
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

        
=======
#look up iterables (what is iterable? generators, enumerate objects)..


# classes:
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print "I AM CLASSY APPLES!"


>>>>>>> External Changes
=======
#look up iterables (what is iterable? generators, enumerate objects)..


# classes:
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print "I AM CLASSY APPLES!"

# call like this:
a = MyStuff()
a.apple()
a.tangerine
>>>>>>> External Changes
=======
#look up iterables (what is iterable? generators, enumerate objects)..


# classes:
class MyStuff(object):  # why object? can put some other word, or key word?
    def __init__(self): # what are the __bla__ things and what do they each do?
        self.tangerine = "And now a thousand years between" 
    def apple(self):
        print "I AM CLASSY APPLES!"

# call like this:
a = MyStuff()
a.apple()
a.tangerine
>>>>>>> External Changes
=======
#look up iterables (what is iterable? generators, enumerate objects)..


# classes:
class MyStuff(object):  # why object? can put some other word, or key word?
    def __init__(self): # what are the __bla__ things and what do they each do?
        self.tangerine = "And now a thousand years between" 
    def apple(self):
        print "I AM CLASSY APPLES!"

# call like this:
a = MyStuff()
a.apple()
print a.tangerine
>>>>>>> External Changes
=======
#look up iterables (what is iterable? generators, enumerate objects)..


# classes:
class MyStuff(object):  # why object? can put some other word, or key word?
#    def __init__(self): # what are the __bla__ things and what do they each do?
#        self.tangerine = "And now a thousand years between" 
    def apple(self):
        print "I AM CLASSY APPLES!"

# call like this:
a = MyStuff()
a.apple()
print a.tangerine
>>>>>>> External Changes
=======
#look up iterables (what is iterable? generators, enumerate objects)..


# classes:
class MyStuff(object):  # why object? can put some other word, or key word?
    def __init__(self): # what are the __bla__ things and what do they each do?
        self.tangerine = "And now a thousand years between" 
    def apple(self):
        print "I AM CLASSY APPLES!"

# call like this:
a = MyStuff()
a.apple()
print a.tangerine
>>>>>>> External Changes
=======
#look up iterables (what is iterable? generators, enumerate objects)..


# classes:
class MyStuff(object):  # why object?
    # 'self' must be identified.
    def __init__(self): # what are the __bla__ things and what do they each do? 
        self.tangerine = "And now a thousand years between"  
    def apple(self):
        print "I AM CLASSY APPLES!"

# call like this:
a = MyStuff()
a.apple()
print a.tangerine
>>>>>>> External Changes
