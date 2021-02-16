from s4_45_p import *

def s4_45_n(n):
    return str(s4_45_n_f(n))[1:-1]
    
def s4_45_n_f(n):
    d = []
    for i in range(1, n+1):
        d.append( 
            h(n, Box(p(0)) |OR| Box(Dia(Not(p(0))))) |OR|
            Not(h(i, A4())) |OR|
            Not(h(i, A4(p0=Dia(p(0))))) |OR| Not(h(i, T())) |OR|
            Not(h(i, A4(p0 = Box(p(0)) |IMPLIES| p(0)))) |OR|
            Not(h(i, T(p0  = Box(p(0)) |IMPLIES| p(0))))
        )
    return nnf(list2disj(d))