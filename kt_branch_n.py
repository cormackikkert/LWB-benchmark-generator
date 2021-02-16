from k_branch_p import *

def kt_branch_n(n):
    return str(kt_branch_n_f(n))[1:-1]

def kt_branch_n_f(n):
    return Not(
        p(100) |AND| Not(p(101)) |AND| mbox(n, bdepth(n) |AND| det(n) |AND| branching(n))
    )