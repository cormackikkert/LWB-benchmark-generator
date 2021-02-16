from k_t4p_p import *

def C(i):
    if i == 0:
        p1 = p(0) |AND| Dia(Not(p(3)))
        return Box( Dia(Box(Dia(p(0)))) |AND| p(0) |IMPLIES| Box(p1) ) |AND| Box(Dia(p1))
    return Dum(p0=p(1)) |AND| Box(C(i-1))

def s4_t4p_p(n):
    return str(s4_t4p_p_f(n))[1:-1]

def s4_t4p_p_f(n):
    return E(n) |OR| nnf(Not(C(2*n-1))) |OR| Dia(p(4))
