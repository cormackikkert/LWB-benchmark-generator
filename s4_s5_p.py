from defs import *

def s4_s5_p(n):
    return str(s4_s5_p_f(n))[1:-1]

def s4_s5_p_f(n):
    d = []
    for i in range(1, 3 * n - 2+1):
        d.append(p(i) |IFF| p(i+1))
    return Box(Dia( Box(list2disj(d)) |OR| Box(p(3*n)) |OR| f(1, 3 * n - 1) )) |OR| Box(Dia(p(1)) |IMPLIES| Not(p(3*n)))


def f(i, n):
    if i == n:
        return FALSE
    return Dia((p(i) |AND| Not(p(i+1))) |OR| (Not(p(i)) |AND| p(i+1))) |OR| Box(f(i+1, n))