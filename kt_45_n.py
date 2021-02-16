from defs import *

def kt_45_n(n):
    return str(kt_45_n_f(n))[1:-1]

def kt_45_n_f(n):
    d = []
    for i in range(1, n+1):
        d.append(mbox(n, Box(p(0)) |OR| Box(Dia(Not(p(0))))) |OR| Not(mbox(i, A4())) |OR|
            Not(mbox(i, A4(p0=Dia(p(0))))) |OR| Not(mbox(i, T())) |OR| 
            Not(mbox(i, A4(p0=Dia(p(0)) |IMPLIES| p(0)))) |OR| 
            Not(mbox(i, A4(p0=Box(p(0)) |IMPLIES| p(0)))))
    return nnf(list2disj(d))

