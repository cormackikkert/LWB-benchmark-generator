from defs import *

def kt_poly_p(n):
    return str(kt_poly_p_f(n))[1:-1]

def kt_poly_p_f(n):
    if n % 2 == 1:
        return poly(5 * n)
    else:
        return poly(5 * n + 1)

@memoized
def poly(n):
    c1 = []
    for i in range(1, n+1+1):
        c1.append(p(i))
    c2 = []
    for i in range(1, n+1+1):
        c2.append(Not(p(2*i)))
    return mbox(n+1, list2conj(c1)) |OR| f(n, n) |OR| mbox(n+1, list2conj(c2))

@memoized
def f(i, n):
    if i == 0: return FALSE
    if i == n: return Dia(f(n-1, n) |OR| mdia(n+2, p(n) |IFF| p(1))) |OR| Box(p(n+2))
    return Dia(f(i-1, n) |OR| mdia(i+2, p(i) |IFF| p(i+1))) |OR| Box(p(i+2))