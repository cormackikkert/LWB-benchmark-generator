from k_grz_p import *

def kt_grz_p(n):  
    return str(kt_grz_p_f(n))[1:-1]

def kt_grz_p_f(n):
    C = Box(p(2) |IMPLIES| Box(p(2))) |IMPLIES| p(2)
    d = []
    for i in range(1, n-1+1): d.append(l(i))

    a1 = Box(Grz(p0=p(2))) |AND| list2conj(d) |AND| Grz(p0=C |AND| A4(p0=C))
    a2 = Grz1(p0=p(1)) |OR| (Grz1(p0=p(2)) |AND| Dia(Box(Not(p(0))))) |OR| Grz1(p0=p(3)) |OR| (Grz1(p0=p(2)) |AND| Dia(p(0)))
    return a1 |IMPLIES| a2      