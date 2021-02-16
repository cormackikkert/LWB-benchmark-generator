from defs import *

@memoized
def l(i):
    if (i % 4 == 0): return Grz1(p0=l2(i//4))
    if (i % 4 == 1): return Grz1(p0=Box(l2(i//4)) |OR| p(1))
    if (i % 4 == 2): return Grz1(p0=Box(l2(i//4)) |OR| p(1) |OR| p(2))
    return Grz1(p0=Box(l2(i//4)) |OR| p(1) |OR| p(2) |OR| p(3))

@memoized
def l2(i):
    if i == 0: return FALSE
    return Box(l2(i-1)) |OR| p(1) |OR| p(2) |OR| p(3) |OR| p(4)

def k_grz_n(n):
    C = Box(p(2) |IMPLIES| Box(p(2))) |IMPLIES| p(2)
    d = []
    for i in range(1, n-1+1):
        d.append(l(i))
    
    res = (Box(Grz1(p0=p(2))) |AND| list2conj(d) |AND| Grz1(p0 = C |AND| A4(p0=C))) |IMPLIES| (Grz(p0=p(1)) |OR| Grz(p0=p(2)) |OR| Grz(p0=p(3)))
    return str(res)[1:-1]
