# like scripts with argv
def print_two(*monkeys):
    arg1, arg2 = monkeys
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r") % (arg1, arg2)
    
def print_one(arg1):
    print "arg11: %r" % arg1

def print_none():
    print "I got nothin."
    
print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("first")
print_none()
    
    