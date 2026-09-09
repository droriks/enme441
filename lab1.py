# ENME 441 - Lab 1: Python Loops
#
# Fill in the functions below, following the assignment handout.  Each def
# line still needs its arguments -- work out from the handout what they are
# and what order they go in.  Do not change the function names, and submit
# this file without renaming it.


def ln_taylor_terms(x, n):
    """Return the approximation of f(x) for a fixed number of terms."""
    # YOUR CODE HERE
    total = 0
    for i in range(1, n+1):
        total += (-1)**(i+1)*(x-1)**i/i
    return total


def ln_taylor_tol(x, tol):
    """Return the approximation of f(x) and the number of terms used."""
    # YOUR CODE HERE
    k = 0
    #arbitrary start term for tol
    term = tol + 1
    total = 0
    while abs(term) > tol:
        k += 1
        term = (-1)**(k+1)*(x-1)**k/k
        total += term
    return total, k


# The code below runs only when this file is executed directly.  It does not run when the autograder imports
# your functions.  Leave it as-is.
if __name__ == '__main__':

    x = 0.5

    approx = ln_taylor_terms(x, 5)
    print(f'f({x}) ~= {approx:.9f} with 5 terms')

    approx, k = ln_taylor_tol(x, 1e-7)
    print(f'f({x}) ~= {approx:.9f} with {k} terms')
