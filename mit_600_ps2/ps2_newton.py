# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # Defense
    assert len(poly)>0
    x = float(x)

    total=0
    for i in range(len(poly)):
        #print(poly[i]*x**i)
        total+=poly[i]*x**i
        
    return total

def evaluate_poly_check(poly, x):
    """
    simple checker
    """
    # Defense
    assert len(poly)>0
    x = float(x)
    return evaluate_poly_r(poly, x)

def evaluate_poly_r(poly, x):
    """
    recursive vertion
    """
    length = len(poly)
    #Base case
    if length == 1:
        return poly[0]
    #Recursive case
    else:        
        return evaluate_poly_r(poly[:-1], x)+poly[-1]*x**(length-1)
        

##poly = (0.0, 0.0, 5.0, 9.3, 7.0, 5.0, 6.7, 4.8, 5.5, 5.0, 9.3, 7.0, 5.0, 6.7, 4.8, 5.5, 5.0, 9.3, 7.0, 5.0, 6.7, 4.8, 5.5)
##x = -13
##import cProfile
##cProfile.run('evaluate_poly_check(poly, x)')
##cProfile.run('evaluate_poly(poly, x)')
##print(evaluate_poly_check(poly, x))
##print(evaluate_poly(poly, x))

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # Defense
    length = len(poly)
    assert length>0
    if length<2:
        return (0.0,)
    else:
        derivative = ()
        for i in range(1,length):
            derivative += (float(i*poly[i]),)
        return derivative

##poly = (-13.39,0.0, 17.5, 3.0, 1)
##print(compute_deriv(poly))      

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # Defense
    length = len(poly)
    assert length>1
    x = float(x_0)
    epsilon = float(epsilon)

    i=1
    fx = evaluate_poly(poly, x)
    while abs(fx)>=epsilon:
        deriv_poly = compute_deriv(poly)
        fx_deriv = evaluate_poly(deriv_poly, x)
        x = x - fx/fx_deriv
        fx = evaluate_poly(poly, x)
        i+=1
    return (float(x),i)

##poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
##x_0 = 0.1
##epsilon = .0001
##print(compute_root(poly, x_0, epsilon))




