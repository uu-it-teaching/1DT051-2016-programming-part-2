'''
Tests for the functions in the mandatory.py module
'''

from mandatory import *

print
print "========== mandatory.py =========="

# ===== is_odd()
print

n = 1
print "id_odd(%d) --> %s" % (n, is_odd(n))
n = 22
print "id_odd(%d) --> %s" % (n, is_odd(n))
n = 31
print "id_odd(%d) --> %s" % (n, is_odd(n))

# is_even()
print

n = 1
print "id_even(%d) --> %s" % (n, is_even(n))
n = 22
print "id_even(%d) --> %s" % (n, is_even(n))
n = 31
print "id_even(%d) --> %s" % (n, is_even(n))


# ith()
print

xs = ['apa', 22, 'bosse', 127]
i = 2
print "ith(%s, %d) --> %s" % (xs, i, ith(xs,i))
i = -1
print "ith(%s, %d) --> %s" % (xs, i, ith(xs,i))

# set_ith()
print

str = "BOSSE"
i = 2
print "set_ith(%s, %i, '%s') --> " % (xs, i, str)
set_ith(xs, i, str)
print xs

# take()
print

xs = [1,2,3,4,5]
n = 3
print "take(%s, %s) --> %s " % (xs, n, take(n, xs)) 

# print_powers_of_two()
print

print_powers_of_two(5)

# length()
print

xs = []
print "length(%s) --> %d" % (xs, length(xs))
xs = [1,2,3]
print "length(%s) --> %d" % (xs, length(xs))

# sum()
print

xs = []
print "sum(%s) --> %s" % (xs, sum(xs))
xs = [1,2,3,4,5,6,7,8,9,10]
print "sum(%s) --> %s" % (xs, sum(xs))

# print_all()
print
xs = ['one', 2, 'three']
print "print_all(%s)" % xs
print_all(xs)

# print_double()
print

ns = [1,2,3,4,5]
print "print_double(%s) -->" % ns
print_double(ns)

# max()
print

print "max(%s) --> %s" % (ns, max(ns))

# print_odd()
print

print "print_odd(%s) -->" % ns
print_odd(ns)

# print_even()
print

print "print_even(%s) -->" % ns
print_even(ns)

