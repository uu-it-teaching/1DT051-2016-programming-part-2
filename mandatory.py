'''
Information Technology (1DT051) 2016

Programming part 2 - assignment.

A collection of mandatory exercises on the following topics:

* Predicate functions, functions taking an argument and returning
  True of False.

* Indexing lists.

* Lists and slice notation.

* Iteration over lists using while.

* Iteration over lists using for-in.

You must add code at all places marked with TODO.
'''

__author__  = "Karl Marklund"
__email__   = "karl.marklund@it.uu.se"


# Import all functions from the utils module.

from utils import *


# ==============================================================================
#                             Predicate functions
# ==============================================================================

# NOTE: A predicate functions takes a single argument and returns a boolean
# value (True or False).


def is_odd(n):
    '''
    Arguments:

    n :: int

    Return :: bool
        If n is odd, returns True and otherwise returns False.

    Example:
    >>> is_odd(0)
    False
    >>> is_odd(1)
    True
    is_odd(2)
    False
    '''

    return True # TODO: You must change this! TIP: Use the modulo operator % to
                # check if the reminder when dividing by 2 is equal to 1.

def is_even(n):
    '''
    Arguments:

    n :: int

    Return :: bool
        If n is even, returns True and otherwise returns False.

    Example:

    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    '''

    return True # TODO: You must change this! You use should is_odd() as part of
                # your solution.


# ==============================================================================
#                             Indexing lists
# ==============================================================================

def ith(xs, i):
    '''
    Arguments:

    xs :: list

    i :: int

    Returns:
        If i is a valid index, return the element at index i in xs.

    Examples:

    >>> xs = ["a", "b", "c"]
    >>> ith(xs, 0)
    'a'
    >>> ith(xs, 1)
    'b'
    >>> ith(xs, 2)
    'c'
    >>> ith(xs, -1)
    'c'
    >>> ith(xs, -2)
    'b'
    >>> ith(xs, -3)
    'a'
    >>> ith(xs, 100)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in ith
    IndexError: list index out of range
    >>>
    '''

    return -999 # TODO: You must change this! TIP: Use square bracket notation
                # to get the value at index i in the list xs.


def set_ith(xs, i, value):
    '''Arguments:

    xs :: list

    i :: int

    value :: Any type of value.

    Returns:
        If i is a valid index, return xs but with the value of
        the element at index i in xs replaced with value.

    Side effects:
        The original list xs is updated in place.

    Examples:

    >>> xs = ["a", "b", "c"]
    >>> set_ith(xs, 1, "B")
    ['a', 'B', 'c']
    >>> set_ith(range(10), 3, "foo")
    [0, 1, 2, 'foo', 4, 5, 6, 7, 8, 9]
    >>>

    '''

    # TODO: You must add code here.

    # TIP: Use square bracket notation and index to update the list xs.

    return xs


# ==============================================================================
#                        Lists and slice notation
# ==============================================================================


def take(n, xs):
    '''
    Arguments:

    n :: int

    xs :: list

    Returns :: list
        A new list with the n first consecutive elements from xs.
        If there is not enough elements in xs, the new list
        will have less than n elements.

    Examples:

    >>> l = [0,1,2,3,4]
    >>> take(0, l)
    []
    >>> take(1, l)
    [0]
    >>> take(2, l)
    [0, 1]
    >>> take(32, l)
    [0, 1, 2, 3, 4]
    '''

    return xs # TODO: You must change this! TIP: Use slice notation.



# ==============================================================================
#                       Iteration over lists using while
# ==============================================================================

def print_powers_of_two(limit):
    '''
    Arguments:

    limit :: int

    Side effects:
       Print a table with the power of two for 2^0, 2^1, ..., 2^limit.

    Example:

    >>> print_powers_of_two(4)
    2^0 = 1
    2^1 = 2
    2^2 = 4
    2^3 = 8
    2^4 = 16
    '''

    n = 0

    while False: # TODO: you must change this.

        print_power_of_two(n) # This functions is defined in utils.py

        # TODO: You must increment n here.



# ==============================================================================
#                      Iteration over lists using for-in
# ==============================================================================

def length(xs):
    '''
    Arguments:

    xs :: list

    Returns :: int
        The number of elements in xs.
    '''

    n = 0

    # TODO: You must add code here.

    # NOTE: You may not use the built-in function len().

    # TIP: Use for-in to iterate through all elements of the list xs and
    # increment n.

    return n

def sum(ns):
    '''Arguments:

    ns :: list of numbers.

    Returns :: number (int or float)
        The sum of all numbers in ns.

    Examples:

    >>> sum([])
    0
    >>> ns = [0, 1, 7, 66, 9, 10, 3]
    >>> sum(ns)
    96

    '''

    s = 0

    # TODO: You must add code here.

    # TIP: Use for-in to iterate through all elements of the list ns and update
    # s.

    return s


def print_all(xs):
    '''
    Arguments:

    xs :: list

    Side effects:

    Print each element x in xs  on a separate line.

    Example:

    >>> xs = [1, 2, 3]
    >>> print_all(xs)
    1
    2
    3
    '''

    print "To be implemented" # TODO: You must change this! TIP: Use for-in to
                              # iterate through all elements in the list xs.


def print_double(ns):
    '''
    Arguments:

    ns :: list of int or float

    Side effects:
        For each element n in ns, prints 2*n on a separate line.

    Example

    >>> ns = [1, 2, 3]
    >>> print_double(ns)
    2
    4
    6
    '''

    print "To be implemented" # TODO: You must change this!

    # NOTE: You must use the function double() from the utils module as part of
    # your solution.

    # TIP: Use for-in to iterate through all elements in ns.


def max(ns):
    """
    Arguments:

    ns :: list of numbers

    Returns the largest number in ns. Returns None if ns is empty.

    Example:

    >>> ns = [9, 2, 1, 17, 2, 11]
    >>> max(ns)
    17
    """

    max = None

    # TODO: You must add code here.

    # NOTE: Your solution should use iteration (for-in).


    return max

def print_odd(ns):
    '''
    Arguments:

    ns :: list of of integers

    Side effects:
        Prints all odd numbers in ns on a separate line.

    Example:

    >>> l = [0, 1, 7, 66, 9, 10, 3]
    >>> print_odd(l)
    1
    7
    9
    3
    '''

    print "To be implemented" # TODO: You must change this.

    # NOTE: You must use is_odd() as part of you solution.

    # TIP: Use for-in to iterate through all elements in ns.

def print_even(ns):
    '''
    Arguments:

    ns :: list of of integers

    Side effects:
        Prints all even numbers in ns on a separate line.

    Example:

    >>> l = [0, 1, 7, 66, 9, 10, 3]
    >>> print_evenl)
    0
    66
    10
    '''

    print "To be implemented" # TODO: You must change this.

    # NOTE: You must use is_even() as part of your solution.

    # TIP: Use for-in to iterate through all elements in ns.


def replace_odds(ns, replacement):
    '''
    Arguments:

    ns :: list of numbers

    replacement :: any data type

    Side effect:
        Replace each odd number in ns with replacement.

    Return value :: list
        Returns ns where all odd numbers have been replaced with replacement.

    Example:

    >>> replace_odds([1,2,3,4], 'odd')
    ['odd', 2, 'odd', 4]
    '''

    # TODO: You must add code here.

    # TIP: Use for-in to iterate through the elements of ns.

    # TIP: Use is_odd to check if an element of ns is an odd number.

    return ns

def repeat(x, n):
    '''
    Arguments:

    x :: any data type

    n :: int

    Return value :: list
        Returns a new list of length n where all elements are equal to x.

    Example:

    >>> repeat(127, 5)
    [127, 127, 127]
    >>> repeat('*', 10)

    '''

    xs = []

    # TODO: You must add code here.

    # TIP: Create a list with n elements using range and use for-in to iterate
    # through this list.

    # TIP: Use xs.append(x) to append a new element x to xs.

    return xs

def lengths(xss):
    '''
    Argument:

    xss :: list of lists

    Returns :: list
        Returns a list of lists lengths for each list in xss.

    Example:

    >>> xss = [[], [1], [1,2], ['apa', 'bosse', 77]]
    >>> lenghts(xss)
    [0, 1, 2, 3]
    '''

    ls = []

    # TODO: You must add code here.

    return ls
