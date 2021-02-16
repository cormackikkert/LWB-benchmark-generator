from k_ph_n import *

def kt_ph_n(n):
    return str(kt_ph_n_f(n))[1:-1]

def kt_ph_n_f(n):
    return left(n) |IMPLIES| Dia(right(n))
