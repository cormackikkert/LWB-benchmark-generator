from defs import *

def kt_path_p(n):
    return str(kt_path_p_f(n))[1:-1]

def kt_path_p_f(n):
    d1 = []
    for i in [1, path_el(1, n), 3, 5]: d1.append(Box(p(10+i)))
    d2 = []
    for i in range(1, n+1):
        for j in range(1, 6+1):
            d2.append(left_to_right(i, j, n) |OR| right_to_left(i, j, n))
    d3 = []
    for i in [2, 4, path_el(n, n), 6]: d3.append(mdia(n, Not(p(10*n+i))))

    return list2disj(d1) |OR| list2disj(d2) |OR| list2disj(d3)

def lists2fml(level, k, s):
    d = []
    for x in s: d.append(mdia(level, Not(p(10*level+k)) |AND| Box(p(10*(level+1) + x))))
    return list2disj(d)

def lists2fml_back(level, k, s):
    d = []
    for x in s: d.append(mdia(level, Not(p(10*level+x)) |AND| Box(p(10*(level+1) + k))))
    return list2disj(d)

@memoized
def delete(x, y1, y2, y3):
    if x == y1: return [y2, y3]
    if x == y2: return [y1, y3]
    if x == y3: return [y1, y2]
    return [y1, y2, y3]

@memoized
def right_to_left(level, k, n):
    if level == 1: return FALSE
    if k%2 == 1: return FALSE
    x = path_el(level - 1, n)
    return lists2fml_back(level - 1, k, delete(x, 2, 4, 6))

@memoized
def left_to_right(level, k, n):
    if level == n: return FALSE
    if (k%2 == 0) and (k != path_el(level, n)): return FALSE
    x = path_el(level + 1, n)
    if (k%2 == 0): return lists2fml(level, k, [x])
    if (k == path_el(level, n)): return lists2fml(level, k, [1, 3, x, 5])
    return lists2fml(level, k, delete(x, 1, 3, 5))

@memoized
def path_el(level, n):
    if level == 1: return 2
    if level > n//2:
        x = path_el(level - 1, n) + 3
    else:
        x = path_el(level - 1, n) + 5
    if x > 6: x = x - 6
    return x
