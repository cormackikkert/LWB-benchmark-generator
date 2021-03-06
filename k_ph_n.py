from defs import *

def k_ph_n(n):
    return Dia(left(n)) |IMPLIES| Dia(right(n))

@memoized
def left(n):
    c = []
    for i in range(1, n+1+1):
        d = []
        for j in range(1, n+1): d.append(l(i, j))
        c.append(list2disj(d))
    return list2conj(c)

@memoized
def right(n):
    d = []
    for j in range(1, n+1):
        for i1 in range(1, n+1+1):
            for i2 in range(i1+1, n+1+1):
                d.append(l2(n, i1, j) |AND| l2(n, i2, j))
    return list2disj(d)

@memoized
def l2(n, i, j):
    if (i == j) and (i == (2*n)//3+1): 
        return Not(l(i, j))
    return l(i, j)

@memoized
def l(i, j):
    if i < j: 
        return Box(p (i * 100 + j))
    else:
        return p(i * 100 + j)