from k_t4p_p import *

def kt_t4p_p(n):
    return str(kt_t4p_p_f(n))[1:-1]

def kt_t4p_p_f(n):
    return E(n) |OR| nnf(Not(C(n))) |OR| Dia(p(4))

@memoized
def C(i):
    if i == 0:
        p1 = p(0) |AND| Dia(Not(p(3)))
        return ((Box(Dia(p(0))) |IMPLIES| Box(Box(Dia(p1)))) |AND|
            Box( Dia(Box(Dia(p(0)))) |AND| p(0) |IMPLIES| Box(p1) ) |AND|
            Box( Dia(p1)))
    return Box(A4(p0=p(1))) |AND| Box(C(i-1))