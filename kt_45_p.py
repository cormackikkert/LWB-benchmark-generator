from defs import *

def kt_45_p(n):
    return str(kt_45_p_f(n))[1:-1]

def kt_45_p_f(n):
    d = []
    for i in range(1, n+1):
        d.append(mbox(n, A4()) |OR| Not(mbox(i, D2())) |OR|
            Not(mbox(i, A5(p0=Dia(Not(p(0)))))) |OR| Not(mbox(i, Box(A5()))) |OR| Not(mbox(i, B())))
    return nnf(list2disj(d))