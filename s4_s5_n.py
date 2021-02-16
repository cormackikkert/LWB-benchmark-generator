from s4_s5_p import *

def s4_s5_n(n):
    return str(s4_s5_n_f(n))[1:-1]

def s4_s5_n_f(n):
    return Box(Dia(Box(p(6*n)) |OR| f(1, 6*n-5) )) |OR| Box( Dia(p(1)) |IMPLIES| Not(p(6*n)) )