from sys import argv

script, fn = argv

print "we're going to erase %r." % fn
print "if you don't want that, hit CTRL-C (^C)."
print "if you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(fn, 'w')

print "truncating the file. goodbye!"
target.truncate()

print "now, i'll ask for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print ("i'll now write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "and finally, we close it."
target.close()


