from s4_t4p_p import *

def C(i):
    if i == 0:
        p1 = p(0) |AND| Dia(Not(p(3)))
        return (Box(Dia(p(0))) |IMPLIES| Dia(p1)) |AND| Box( Dia(Box(Dia(p(0)))) |AND| p(0) |IMPLIES| Box(p1) )
    return Dum(p0=p(1)) |AND| Box(C(i-1))

def s4_t4p_n(n):
    return str(s4_t4p_n_f(n))[1:-1]

def s4_t4p_n_f(n):
    return E(2*n-1) |OR| nnf(Not(C(4*n-1))) |OR| Dia(p(4))

