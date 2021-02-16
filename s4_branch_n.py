from k_branch_p import *

def s4_branch_n(n):
    return str(s4_branch_n_f(n))[1:-1]

def s4_branch_n_f(n):
    return Not(p(100) |AND| Not(p(101)) |AND| Box(bdepth(n) |AND| det(n) |AND| branching(n)))