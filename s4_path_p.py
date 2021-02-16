from kt_path_p import *

def s4_path_p(n):
    return str(s4_path_p_f(n))[1:-1]

def s4_path_p_f(n):
    d1 = []
    for i in [1, path_el(1, n), 3, 5]: d1.append(Box(Box(p(10+i))))
    d2 = []
    for i in range(1, n+1):
        for j in range(1, 6+1):
            d2.append(left_to_right(i, j, n) |OR| right_to_left(i, j, n))
    d3 = []
    for i in [2, 4, path_el(n, n), 6]: d3.append(Dia(Not(p(10*n+i))))
    return list2disj(d1) |OR| list2disj(d2) |OR| Dia(list2disj(d3))