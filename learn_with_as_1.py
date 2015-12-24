
#def controlled_execution(callback):
#        set things up
#        try:
#           callback(thing)
#        finally:
#            tear things down
#
#def my_function(thing):
#    do something

#controlled_execution(my_function)

#with open("ex10.py") as f:
#    data = f.read()
#    print data
	

	
try:
	1.0/0
except ZeroDivisionError:
    print "monkey error"
else:
    print "okay"
finally:
    print "finishing now."
	
	