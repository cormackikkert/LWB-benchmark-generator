from defs import *

def k_dum_n(n):
    c = A4(p0 = (Box(p(0) |IMPLIES| Box(p(0))) |IMPLIES| p(0))) |AND| Box(A4()) |AND| Dum4() |AND| Dum4(p0 = (p(0) |IMPLIES| Box(p(0))))
    
    d1 = []
    for i in range(1, n//2+1):
        d1.append(mbox(i, Box(A4()) |AND| Dum4()))
    
    d2 = []
    for i in range(n//2+2, n-1+1):
        d2.append(mdia(i, Not(Box(A4()) |AND| Dum4())))

    return str((list2conj(d1) |AND| Not(mbox(n+1, Dum())) |IMPLIES| (mdia(n+1, Not(c)) |OR| list2disj(d2))))[1:-1]
