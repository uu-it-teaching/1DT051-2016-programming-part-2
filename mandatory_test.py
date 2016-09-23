'''
Tests for the functions in the mandatory.py module
'''

from mandatory import *

def main():
    '''Run all tests.'''

    is_odd_test()
    is_even_test()
    ith_test()
    set_ith_test()
    take_test()
    print_powers_of_two_test()
    length_test()
    sum_test()
    print_all_test()
    print_double_test()
    max_test()
    print_odd_test()
    print_even_test()
    replace_odds_test()
    repeat_test()
    lengths_test()

def is_odd_test():
    print
    n = 1
    print "id_odd(%d) --> %r" % (n, is_odd(n))
    n = 22
    print "id_odd(%d) --> %r" % (n, is_odd(n))
    n = 31
    print "id_odd(%d) --> %r" % (n, is_odd(n))


def is_even_test():
    print
    n = 1
    print "is_even(%d) --> %r" % (n, is_even(n))
    n = 22
    print "is_even(%d) --> %r" % (n, is_even(n))
    n = 31
    print "is_even(%d) --> %r" % (n, is_even(n))


def ith_test():
    print
    xs = ['apa', 22, 'bosse', 127]
    i = 2
    print "ith(%r, %d) --> %r" % (xs, i, ith(xs,i))
    i = -1
    print "ith(%r, %d) --> %r" % (xs, i, ith(xs,i))

def set_ith_test():
    print
    xs = ['apa', 22, 'bosse', 127]
    str = "BOSSE"
    i = 2
    print "set_ith(%r, %i, %r) --> " % (xs, i, str)
    set_ith(xs, i, str)
    print xs

def take_test():
    print
    xs = [1,2,3,4,5]
    n = 3
    print "take(%r, %r) --> %r " % (xs, n, take(n, xs))


def print_powers_of_two_test():
    print
    print_powers_of_two(5)


def length_test():
    print
    xs = []
    print "length(%r) --> %d" % (xs, length(xs))
    xs = [1,2,3]
    print "length(%r) --> %d" % (xs, length(xs))

def sum_test():
    print
    xs = []
    print "sum(%r) --> %r" % (xs, sum(xs))
    xs = [1,2,3,4,5,6,7,8,9,10]
    print "sum(%r) --> %r" % (xs, sum(xs))

def print_all_test():
    print
    xs = ['one', 2, 'three']
    print "print_all(%r)" % xs
    print_all(xs)

def print_double_test():
    print
    ns = [1,2,3,4,5]
    print "print_double(%r) -->" % ns
    print_double(ns)

def max_test():
    print
    ns = [1,2,3,4,5]
    print "max(%r) --> %r" % (ns, max(ns))

def print_odd_test():
    print
    ns = [1,2,3,4,5]
    print "print_odd(%r) -->" % ns
    print_odd(ns)

def print_even_test():
    print
    ns = [1,2,3,4,5]
    print "print_even(%r) -->" % ns
    print_even(ns)

def replace_odds_test():
    print
    ns = range(10)
    print "replace_odds(%r) --> " % ns
    print ns

def repeat_test():
    print
    x = 127
    n = 5
    print "repeat(%r, %r) --> %r" % (x, n, repeat(x, n))

def lengths_test():
    print
    xss = [[], [1], ['apa', 'bosse', 77]]
    print "lengths(%r) --> %r" % (xss, lengths(xss))

if __name__ == "__main__":
    main()
