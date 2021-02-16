from defs import *

def s4_45_p(n):
    return str(s4_45_p_f(n))[1:-1]

def s4_45_p_f(n):
    d = []
    for i in range(1, n+1):
        d.append(h(n,A5()) |OR| Not(h(i, D2())) |OR| 
            Not(h(i, A5(p0=Dia(Not(p(0)))))) |OR| 
            Not(h(i, Box(A5()))) |OR|
            Not(h(i, B())))
    return nnf(list2disj(d))

def h(i, a):
    if i == 0: return a
    return Box(p(0)) |OR| Box(h(i-1, a)) |OR| Box(p(1))