import datetime

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I said %s." % y
hilarious = False
joke_evaluation = "isn't this joke aaweome! %r"
percentS = "percentS! %s"
percentR = "percentSR! %r"

print percentS % datetime.date.today()
print percentR % datetime.date.today()


print joke_evaluation % hilarious

print joke_evaluation % 'fuck you'

print joke_evaluation 

w = "this is the left"
e = "side of a string"
print w + e
print w, e


