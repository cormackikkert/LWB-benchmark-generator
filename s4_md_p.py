from defs import *

def s4_md_p(n):
    return str(s4_md_p_f(n))[1:-1]

def s4_md_p_f(n):
    d = []
    for i in range(1, n-1+1):
        d.append(g(i, n, Not(p(1)) |AND| Dia(f(1, n, p(2)))) |OR|
                    g(i, n, Not(p(1)) |AND| Dia(f(1, n, p(1)))) |OR|
                    g(i, n, Not(p(2)) |AND| Dia(f(1, n, p(1)))))
    return p(1) |OR| list2disj(d) |OR| g(n, n, Not(p(1)))

def g(i, n, a):
    if i == 1: return a
    return f(i, n, g(i-1, n, a))

def f(i, n, a):
    return h(i-1, Box(h(n-i, a)))

def h(i, a):
    if i == 0: return a
    return Dia(h(i-1, a)) |OR| p(2)