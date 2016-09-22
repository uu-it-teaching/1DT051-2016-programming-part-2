'''Information Technology (1DT051) 2016

Programming assignment 2.

This module defines a few useful functions, most of which operates on lists and
strings. You don't need to change or add any code to this module.

'''

__author__  = "Karl Marklund"
__email__   = "karl.marklund@it.uu.se"

def double(n):
    '''
    Arguments:

    n :: int or float

    Returns 2*n
    '''

    return 2*n

def print_power_of_two(n):
    '''
    Arguments:

    n :: int

    Side effect:
        Prints the result of 2^n on a single line.

    Examples:

    >>> print_power_of_two(0)
    2^0 = 1
    >>> print_power_of_two(1)
    2^1 = 2
    >>> print_power_of_two(2)
    2^2 = 4
    >>> print_power_of_two(3)
    2^3 = 8
    >>> print_power_of_two(5)
    2^5 = 32
    >>> print_power_of_two(10)
    2^10 = 1024
    '''

    print "2^%d = %d" % (n, 2**n)


def empty(xs):
    """
    Arguments:

    xs :: list or str

    Returns True if the list or string xs is empty and otherwise
    returns False.

    """

    return len(xs) == 0

def first(xs):
    """
    Alias for head(xs).
    """

    return head(xs)

def head(xs):
    """
    Arguments:

    xs :: list or str

    Returns the first element or character in xs. If xs is empty, None is
    returned.
    """

    return xs[0] if not empty(xs) else None

def tail(xs):
    """
    Arguments:

    xs :: list or str

    Returns a list or string equal to xs but with the first element of xs
    removed.
    """

    return xs[1:]

def last(xs):
    """
    Arguments:

    xs :: list or str

    If xs is a list, returns the last element in xs. If xs is a string,
    returns the last character in a xs.
    """

    return xs[-1] if not empty(xs) else None

def remove_non_letters(s):
    """
    Arguments:

    s :: str

    Returns a string equal to s but with all white space characters and
    inter-punctuation characters removed. That is, the returned
    string will only contains the characters a-z and A-Z.
    """

    return "".join([c for c in s if c.isalpha()])

def clean(s):
    """
    Arguments:

    s :: str

    Returns a string equal to s but with all characters converted to
    to lower case and all inter-punctuation characters removed.
    """

    return remove_non_letters(s.lower())

def middle(xs):
    """
    Arguments:

    xs :: list or str

    Returns a list or string equal to xs but with the first and last elements or
    characters of xs removed.

    """

    return xs[1:-1]

def reverse(xs):
    """
    Arguments:

    xs :: list or str

    Returns a reversed version of the list or string xs.
    """

    # Use a slice to get a reversed copy.

    return xs[::-1]


def transpose(strings):
    """
    Arguments:

    strings :: list of str
        A list of strings.

    Returns:
        A transposed version of strings.

    Example:

        l = ["abcd", "ABCD"]

        for s in l:
            print s

        # Result of printout:

        abcd
        ABCD

        transpose(l) == ['aA', 'bB', 'cC', 'dD']

        for s in transpose(l):
            print s

        # Result of printout:

        aA
        bB
        cC
        dD
    """

    # Unpacking arguments lists using the *-operator

    # http://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
    # http://stackoverflow.com/questions/5239856/foggy-on-asterisk-in-python
    # http://stackoverflow.com/questions/12555627/python-3-starred-expression-to-unpack-a-list

    # zip takes arbitrary many positional arguments. Using the *-operator
    # we can call it with a list of lists.

    # >>> zip("abc", "123", "ABC")
    # [('a', '1', 'A'), ('b', '2', 'B'), ('c', '3', 'C')]
    # >>> zip(*["abc", "123", "ABC"])
    # [('a', '1', 'A'), ('b', '2', 'B'), ('c', '3', 'C')]

    list_of_tuples = zip(*strings)

    list_of_strings = [''.join(s) for s in list_of_tuples]

    return list_of_strings

    # return [''.join(s) for s in map(list, zip(*strings))]
