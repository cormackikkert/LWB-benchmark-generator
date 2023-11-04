from k_branch_p import *

def kt_branch_p(n):
    return kt_branch_p_f(n)

def kt_branch_p_f(n):
    return Not(
        p(100) |AND| Not(p(101)) |AND| mbox(n, bdepth(n) |AND| det(n) |AND| branching(n))
    ) |OR| Not(mbox(n, p(n // 3 + 1)))
