from k_branch_p import *

def s4_branch_p(n):
    return str(s4_branch_p_f(n))[1:-1]

def s4_branch_p_f(n):
    return Not(p(100) |AND| Not(p(101)) |AND| Box(bdepth(n) |AND| det(n) |AND| branching(n))) |OR| Not(Box(p(n//3+1)))