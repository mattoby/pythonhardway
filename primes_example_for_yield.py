# from: https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
# primes ex
import math

#def magical_infinite_range(start):
#    return range(start,1000)

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False
	
#def get_primes(start):
##    for element in magical_infinite_range(start):
 #       if is_prime(element):
 #           return element

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

	
def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1

def print_successive_primes(iterations, base=10): # prints 
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))


# random generators
def generator3():
    out = "initial"
    for n in range(1,10):
        out = yield n
        yield out

def generator1():
    yield 2

def test_generator(number):
    while True:
        print "the pre-yield number is %s" % number
        number = yield number
        print "the post-yield number is %s" % number
        yield number

def testgen():
    for x in xrange(10):
        res = yield
        yield res
