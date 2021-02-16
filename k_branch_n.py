from k_branch_p import *

def k_branch_n(n):
    b = bdepth(n) |AND| det(n) |AND| branching(n)
    l = []
    for i in range(0, n+1):
        l.append(mbox(i, b))
    res = Not(p(100) |AND| Not(p(101)) |AND| list2conj(l))
    return str(res)[1:-1]