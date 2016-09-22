'''
Tests for the functions in the utils.py module
'''

from utils import *

def main():
    '''
    Runs all tests.
    '''

    # Comment out tests you don't want to run.

    double_test()
    print_power_of_two_test()
    empty_test()
    first_test()
    head_test()
    tail_test()
    last_test()
    remove_non_letters_test()
    clean_test()
    middle_test()
    reverse_test()
    transpose_test()


def double_test():
    print
    n = 5
    print "double(%r) = %r" % (n, double(n))
    n = 3.5
    print "double(%r) = %r" % (n, double(n))

def print_power_of_two_test():
    print
    print_power_of_two(0)
    print_power_of_two(1)
    print_power_of_two(5)
    print_power_of_two(10)

def empty_test():
    print
    xs = []
    print "empty(%r) --> %r" % (xs, empty(xs))
    xs = [[]]
    print "empty(%r) --> %r" % (xs, empty(xs))
    xs = [1]
    print "empty(%r) --> %r" % (xs, empty(xs))
    xs = [1,2,3,4]
    print "empty(%r) --> %r" % (xs, empty(xs))

def first_test():
    print
    xs = []
    print "first(%r) --> %r" % (xs, first(xs))
    xs = [1]
    print "first(%r) --> %r" % (xs, first(xs))
    xs = [1,2,3,4]
    print "first(%r) --> %r" % (xs, first(xs))

def head_test():
    print
    xs = []
    print "head(%r) --> %r" % (xs, head(xs))
    xs = [1]
    print "head(%r) --> %r" % (xs, head(xs))
    xs = [1,2,3,4]
    print "head(%r) --> %r" % (xs, head(xs))

def tail_test():
    print
    xs = []
    print "tail(%r) --> %r" % (xs, tail(xs))
    xs = [1]
    print "tail(%r) --> %r" % (xs, tail(xs))
    xs = [1,2,3,4]
    print "tail(%r) --> %r" % (xs, tail(xs))

def last_test():
    print
    xs = []
    print "last(%r) --> %r" % (xs, last(xs))
    xs = [1]
    print "last(%r) --> %r" % (xs, last(xs))
    xs = [1,2,3,4]
    print "last(%r) --> %r" % (xs, last(xs))

def remove_non_letters_test():
    print
    s = ""
    print "remove_non_letters(%r) --> %r" % (s, remove_non_letters(s))
    s = "a1b2c3@4%5_6 7*9"
    print "remove_non_letters(%r) --> %r" % (s, remove_non_letters(s))

def clean_test():
    print
    s = ""
    print "clean(%r) --> %r" % (s, clean(s))
    s = "This, is A@ sentence!"
    print "clean(%r) --> %r" % (s, clean(s))

def middle_test():
    print
    s = ""
    print "middle(%r) --> %r" % (s, middle(s))
    s = "ab"
    print "middle(%r) --> %r" % (s, middle(s))
    s = "abc"
    print "middle(%r) --> %r" % (s, middle(s))
    s = "abcd"
    print "middle(%r) --> %r" % (s, middle(s))

def reverse_test():
    print
    s = ""
    print "reverse(%r) --> %r" % (s, reverse(s))
    s = "ab"
    print "reverse(%r) --> %r" % (s, reverse(s))
    s = "abc"
    print "reverse(%r) --> %r" % (s, reverse(s))
    s = "abcd"
    print "reverse(%r) --> %r" % (s, reverse(s))

def transpose_test():
    print
    ss = ["abcd", "ABCD"]
    print "transpose(%r) --> %r" % (ss, transpose(ss))




if __name__ == "__main__":
    main()
