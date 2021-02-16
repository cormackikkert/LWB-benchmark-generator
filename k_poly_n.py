from k_poly_p import *

def k_poly_n(n):
    if (n%2 == 0):
        res = poly(3 * n)
    else:
        res = poly(3*n+1)
    return str(res)[1:-1]