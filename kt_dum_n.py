from defs import *

def kt_dum_n(n):
    return str(kt_dum_n_f(n))[1:-1]

def kt_dum_n_f(n):
    c = A4(p0 = Box(p(0) |IMPLIES| Box(p(0))) |IMPLIES| p(0)) |AND| Box(A4()) |AND| Dum() |AND| Dum(p(0) |IMPLIES| Box(p(0)))
    d1 = []
    for i in range(1, n//2+1): 
        d1.append(mbox(i, Box(A4()) |AND| Dum()))
    d2 = []
    for i in range(n//2+2, n-1+1):
        d2.append(mdia(i, Not(Box(A4()) |AND| Dum() )))
    return (list2conj(d1) |AND| Not(mbox(n//2+1, Grz()))) |IMPLIES| (mdia(n//2+1, Not(c)) |OR| list2disj(d2))
