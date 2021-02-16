from k_ph_p import *

def right2(n):
    d = []
    for j in range(1, n+1):
        for i1 in range(1, n+1+1):
            for i2 in range(i1+1, n+1+1):
                d.append(Dia(l(i1, j) |AND| l(i2, j)))
    return list2disj(d)

def s4_ph_p(n):
    return str(s4_ph_p_f(n))[1:-1]

def s4_ph_p_f(n):
    return left(n) |IMPLIES| Dia(right2(n))