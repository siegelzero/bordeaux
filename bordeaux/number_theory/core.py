import functools


###########################################################################
# Core functions
############################################################################


def gcd(x, y):
    r"""Returns the greatest common divisor of the given numbers.

    This function uses the Euclidean algorithm to compute the greatest
    common divisor of the integers `x` and `y`.

    Parameters
    ----------
    x : int
    y : int

    Returns
    -------
    d : int
        The greatest common divisor of `x` and `y`.

    See Also
    --------
    gcd_list

    Notes
    -----
    This function uses the classical Euclidean algorithm. If `x` and `y`
    are each of order of magnitude N, it can be shown that the overall
    complexity of the algorithm is O(log(N)^2). This is essentially the
    square of the number of digits in an operand. See section 4.2 of [1]
    for details.

    References
    ----------
    .. [1] Bach, Shallitt, "Algorithmic Number Theory", MIT Press,
       Cambridge, MA, 1996

    Examples
    --------
    >>> gcd(39064, 844)
    4
    >>> gcd(7, 5)
    1
    >>> gcd(-4, 2)
    2
    """
    x = abs(x)
    y = abs(y)

    if x < y:
        x, y = y, x

    while y:
        x, y = y, x % y

    return x


def gcd_list(iterable):
    r"""Returns the greatest common divisor of the given numbers.

    Parameters
    ----------
    iterable : iterable of int

    Returns
    -------
    d : int
        The greatest common divisor of the given integers.

    See Also
    --------
    gcd

    Notes
    -----
    See [2].

    References
    ----------
    .. [2] T.M. Apostol, "Introduction to Analytic Number Theory",
       Springer-Verlag, New York, 1976.

    Examples
    --------
    >>> gcd_list([2, 4, 6])
    2
    >>> gcd_list([7])
    7
    """
    return functools.reduce(gcd, iterable)
