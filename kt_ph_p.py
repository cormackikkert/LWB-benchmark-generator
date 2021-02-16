from k_ph_p import *

def kt_ph_p(n):
    return str(kt_ph_p_f(n))[1:-1]
    
def kt_ph_p_f(n):
    return left(n) |IMPLIES| Dia(right(n))