from defs import *

def k_d4_p(n):
    d = []
    for i in range(1, n+1):
        d.append(mbox(n, T()) |OR| Not(mbox(i, D2())) |OR| Not(mbox(i, A4())) |OR| 
            Not(mbox(i, A4(p0=Dia(p(0))))) |OR| Not(mbox(i, B())) |OR| Not(mbox(i, B(p0=Not(p(0))))))
    return str(nnf(list2disj(d)))[1:-1]