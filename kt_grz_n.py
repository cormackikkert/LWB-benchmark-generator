from kt_grz_p import *

def kt_grz_n(n):
    return str(kt_grz_n_f(n))[1:-1]

def kt_grz_n_f(n):
    C = Box(p(2) |IMPLIES| Box(p(2))) |IMPLIES| p(2)
    d = []
    for i in range(1, n-1+1): d.append(l(i))
    a1 = Box(Grz1(p0=p(2))) |AND| list2conj(d) |AND| Grz1(p0=C |AND| A4(p0=C))
    a2 = A5(p0=p(1)) |OR| A5(p0=p(2)) |OR| A5(p0=p(3))
    return a1 |IMPLIES| a2

@memoized
def l(i):
    if i % 4 == 0: return Grz1(p0=l2(i//4))
    if i % 4 == 1: return Grz1(p0=Box(l2(i//4)) |OR| p(1))
    if i % 4 == 2: return Grz1(p0=Box(l2(i//4)) |OR| p(1) |OR| p(2))
    return Grz1(p0=Box(l2(i//4)) |OR| p(1) |OR| p(2) |OR| p(3))