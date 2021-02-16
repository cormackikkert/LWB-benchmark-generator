from s4_md_p import *

def s4_md_n(n):
    return str(s4_md_n_f(n))[1:-1]

def s4_md_n_f(n):
    d = []
    for i in range(1, n-1+1):
        d.append(g(i, n, Not(p(1)) |AND| Dia(f(1, n, p(1)))))
    return p(1) |OR| list2disj(d)