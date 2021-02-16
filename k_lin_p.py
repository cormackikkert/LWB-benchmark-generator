from defs import *

def H2(p0=p(0), p1=p(1)):
    return H(p0=p0 |AND| Box(p0) |AND| p0 |IMPLIES| p1, p1=Not(p0) |IMPLIES| Not(Box(p1) |AND| p1))

def k_lin_p(n):
    d1 = []
    for i in range(1, n//3+1):
        d1.append(Not(H2(p0=p(i), p1=p(i+1))))
    d2 = []
    for i in range(n//3+1, n+1):
        d2.append(Not(H2(p0=p(i), p1=p(i+1))))
    return str(list2disj(d1) |OR| L(p0=p(n), p1=p(n)) |OR| list2disj(d2))[1:-1]
