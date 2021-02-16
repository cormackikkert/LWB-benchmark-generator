from defs import *

def s4_ipc_p(n):
    return str(s4_ipc_p_f(n))[1:-1]

def s4_ipc_p_f(n):
    c = []
    for i in range(1, n+1): c.append(f(i, n))
    return list2conj(c) |IMPLIES| FALSE

def f(i, n):
    c = []
    for j in range(1, n+1):
        c.append(Box(p(j)))
    return Box(Box(Box(p(i)) |IMPLIES| list2conj(c)) |IMPLIES| FALSE)