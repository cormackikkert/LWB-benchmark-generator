from defs import *

@memoized
def bdepth(n):
    c = []
    for i in range(1, n+1+1):
        c.append(Implies(p(100 + i), p(99+i)))
    return list2conj(c)

@memoized
def det(n):
    c = []
    for i in range(0, n+1):
        c.append(Implies(p(100 + i),
            And(Implies(p(i), Box(Implies(p(100 + i), p(i)))), 
            Implies(Not(p(i)), Box(Implies(p(100 + i),Not(p(i))))))))
    return list2conj(c)

@memoized
def branching(n):
    c = []
    for i in range(0, n-1+1):
        c.append(
            (p(100+i) |AND| Not(p(101+i))) |IMPLIES|
                (Dia(p(101+i) |AND| Not(p(102+i)) |AND| p(i+1)) |AND|
                    Dia(p(101+i) |AND| Not(p(102+i)) |AND| Not(p(i+1))))
        )
    return list2conj(c)

def k_branch_p(n):
    b = And(And(bdepth(n), det(n)), branching(n))
    l = []
    for i in range(0, n+1):
        l.append(mbox(i, b))
    res = Or(Not(And(And(p(100), Not(p(101))), list2conj(l))), Not(mbox(n, p(n // 3 + 1))))
    return str(res)[1:-1]