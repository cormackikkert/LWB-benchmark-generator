from defs import *

def k_t4p_p(n):
    return E(n) |OR| nnf(Not(C(n))) |OR| Dia(p(4))

@memoized
def C(i):
    if i == 0:
        p1 = p(0)|AND| Dia(Not(p(3)))
        res = ((Box(Dia(p(0))) |IMPLIES| Dia(p1)) |AND|
                Box(Box(Not(Box(Dia(p1)))) |IMPLIES| Not(Box(Dia(p(0))))) |AND|
                (Box(Dia(p(0))) |IMPLIES| Box(Box(Dia(p1)))) |AND|
                Box( (Dia(Box(Dia(p(0)))) |AND| p(0)) |IMPLIES| Box(p1)) |AND|
                Box(Dia(p1)))
        return res
    return Box(A4(p0=p(1))) |AND| Box(C(i-1)) |AND| Box(A4(p0=Dia(p(1))))

@memoized
def E(i):
    if i == 0:
        return Dia(Box(p(0)))
    return Dia(Not(A4(p0=Not(p(1))))) |OR| Box(E(i-1)) |OR| Box(A5(p0=p(1)))
