'''
Information Technology (1DT051) 2016

Programming assignment 2.

Optional exercises if you want to explore higher order functions and recursion.
'''

__author__  = "Karl Marklund"
__email__   = "karl.marklund@it.uu.se"

# Import functions from the mandatory.py module.
from mandatory import is_odd, is_even

# Import functions from the utils.py module.
from utils import empty, clean, first, head, middle, last, tail, clean


# ==============================================================================
#                         Higher order functions
# ==============================================================================

def print_if(p, xs):
    '''
    Arguments:

    p :: function
        A predicate function taking an element in the list xs and
        returning a bool.

    xs :: list

    Side effects:
        For each element x in xs for which the predicate p(x)
        returns True, print x.

    Example:

    >>> l = [0, 1, 7, 66, 9, 10, 3]
    >>> print_if(is_odd, l)
    1
    7
    9
    3
    '''

    print "To be implemented" # You must change this!

    # TODO: Add code here.


def filter(p, xs):
    '''
    Arguments:

    p :: function
        A predicate function taking an element in the list xs and
        returning a bool.

    xs :: list
        A list with arbitrary values.

    Returns :: list
        A copy of xs but where all elements x for which p(x)
        returns False removed.

    Example:

    >>> l = [0, 1, 7, 66, 9, 10, 3]
    >>> filter(is_odd, l)
    [1, 7, 9, 3]
    >>> filter(is_even, l)
    [0, 66, 10]
    '''

    filtered = []

    # TODO: You must add code here. You should use iteration (for)
    # over the element in xs. Use filtered.append(x) to append values
    # to the list filtered.



    return filtered

def square(n):
    '''
    Arguments:

    n :: number (int or float)

    Returns the square of n.
    '''

    return x # You must change this.

def map(f, xs):
    '''
    Arguments:

    f :: function
        A function f taking a value x in the list xs as argument and returning
        a the value f(x).

    xs :: list

    Returns :: list
        A list ys such that ys[i] == f(xs[i]), that is, a copy of xs
        where every element x in xs is replaced by y = f(x).

    Example:

    >>> l = [0, 1, 7, 66, 9, 10, 3]
    >>> map(is_odd, l)
    [False, True, True, False, True, False, True]
    >>> map(square, range(10))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>>
    '''

    ys = xs[:]   # A copy of xs

    i = 0        # Index

    # TODO: Add code here. You may not use the built in map()
    # function. You should use iteration (for) over the elements in xs.


    return ys

def even_squares(ns):
    '''
    Arguments:

    ns :: list of int or double

    Returns a copy of ns where each element is squares and all odd
    squares are removed.

    Examples:

    >>> even_squares(range(10))
    [0, 4, 16, 36, 64]
    >>>
    '''

    # TODO: You must add code here. You should combine map(), filter()
    # and square() in your solution.

    return ns # You must change this.



# ==============================================================================
#                             Recursion over strings
# ==============================================================================

def is_palindrome(s):
    '''
    Arguments:

    s :: string

    Returns True if s is a palindrome and otherwise returns False.
    '''

    return is_palindrome_r(clean(s))

def is_palindrome_r(s):
    '''
    A helper function used by is_palindrome().

    Arguments:

    s :: string
       A lower case string with no white-space or inter-punctuation characters.
    '''

    # TODO: Add code here. Use first(), last() and middle() from the
    # utils module, they are already imported.


    return True # You must change this.
                # Add base case(s) and a recursive call to is_palindrome_r().




# ==============================================================================
#                             Recursion over lists
# ==============================================================================

def max_r(ns):
    '''
    Arguments:

    ns :: list of numbers

    Returns the largest number in ns. Returns None if ns is empty.
    '''

    # TODO: Implement a recursive solution. Add base case and call to
    # max_r2() for non base case. Use empty(), head() and tail() from
    # the utils module.


def max_r2(acc, ns):
    '''
    Helper function used by max_r().

    Arguments:

    acc :: number (int or float)

    ns :: list of numbers

    If ns is empty, return the value of acc (the accumulator),
    otherwise make a recursive call to max_r2().
    '''

    # TODO: Add code here. You may not use iteration (for or
    # while). Use head() and tail() from the utils module.
