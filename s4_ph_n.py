from s4_ph_p import *

def s4_ph_n(n):
    return str(s4_ph_n_f(n))[1:-1]
    
def s4_ph_n_f(n):
    return left(n) |IMPLIES| Dia(right3(n))

def right3(n):
    d = []
    for j in range(1, n+1):
        for i1 in range(1, n+1+1):
            for i2 in range(i1+1, n+1+1):
                d.append(Dia(l2(n, i1, j) |AND| l2(n, i2, j)))
    return list2disj(d)

def l2(n, i, j):
    if (i == j) and (i == (2*n)//3 + 1): return Not(l(i, j))
    else: return l(i, j)
    