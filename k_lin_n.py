from defs import *

def k_lin_n(n):
    d1 = []
    for i in range(1, 2*n-2+1):
        d1.append(Not(L(p0=Dia(p(i)), p1=p(i+1))) |OR| Not(L(p0= p(i) |IMPLIES| Box(p(i+1)), p1=p(i+1))))
    d2 = []
    for i in range(2*n, 4*n-4+1):
        d2.append(Not(L(p0=Dia(p(i)), p1=p(i+1))) |OR| Not(L(p0= p(i) |IMPLIES| Box(p(i+1)), p1=p(i+1))))

    return str(list2disj(d1) |OR| Lplus(p0=p(n), p1=p(n)) |OR| list2disj(d2))[1:-1]