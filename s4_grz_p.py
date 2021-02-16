from k_grz_p import *

def s4_grz_p(n):
    return str(s4_grz_p_f(n))[1:-1]

def s4_grz_p_f(n):
    C = Box(p(2) |IMPLIES| Box(p(2))) |IMPLIES| p(2)
    d1 = []
    for i in range(1, n-1+1): d1.append(l(i))
    return (Box(Grz(p0=p(2))) |AND| list2conj(d1) |AND| Grz(p0=C |AND| A4(p0=C))) |IMPLIES| (Grz1(p0=p(1)) |OR| (Grz1(p0=p(2)) |AND| Not(Box(Dia(p(0))))) |OR| Grz1(p0=p(3)) |OR| (Grz1(p0=p(2)) |AND| Not(Dia(Not(Box(Dia(p(0))) |OR| p(1))))))