import sys
import random
sys.setrecursionlimit(2000001)

EXACT = False # If we mimic LWB output exactly
_LOGIC = "K"

class Formula:
    pass

class TRUE_(Formula):
    def __init__(self):
        pass
    def __str__(self):
        return "true"
    def write(self, file):
        file.write("true")

class FALSE_(Formula):
    def __init__(self):
        pass
    def __str__(self):
        return "false"
    def write(self, file):
        file.write("false")

TRUE=TRUE_()
FALSE=FALSE_()

class Lit(Formula):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        if _LOGIC == 'K':
            return f"p{self.num}"
        elif 'KnUnsat' in _LOGIC:
            mod = random.randint(1, 10)
            return f"p{self.num} | (<r{mod}> p{self.num} & [r{mod}] ~p{self.num})"
        elif 'KnSat' in _LOGIC:
            mod = random.randint(1, 10)
            return f"p{self.num} & (<r{mod}> p{self.num} & [r{mod+10}] ~p{self.num})"


    def write(self, file):
        file.write(f"p{self.num}")

class Not(Formula):
    def __init__(self, a1):
        self.a1 = a1

    def __str__(self):
        return f"(~{self.a1})"

    def write(self, file):
        print("WRITING", type(self.a1))
        file.write("~(")
        self.a1.write(file)
        file.write(")")

class And(Formula):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def __str__(self):
        return f"({self.a1} & {self.a2})"

    def write(self, file):
        file.write("(")
        self.a1.write(file)
        file.write(" & ")
        self.a2.write(file)
        file.write(")")

class Or(Formula):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def __str__(self):
        if not EXACT:
            return f"({self.a1.__str__()} | {self.a2.__str__()})"
        return f"({self.a1.__str__()} v {self.a2.__str__()})"

    def write(self, file):
        file.write("(")
        self.a1.write(file)
        file.write(" | ")
        self.a2.write(file)
        file.write(")")

class Implies(Formula):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def __str__(self):
        return f"({self.a1.__str__()} -> {self.a2.__str__()})"

    def write(self, file):
        file.write("(")
        self.a1.write(file)
        file.write(" -> ")
        self.a2.write(file)
        file.write(")")

class Iff(Formula):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    
    def __str__(self):
        return f"({self.a1.__str__()} <-> {self.a2.__str__()})"

    def write(self, file):
        file.write("(")
        self.a1.write(file)
        file.write(" <-> ")
        self.a2.write(file)
        file.write(")")

class Box(Formula):
    def __init__(self, a1):
        self.a1 = a1

    def __str__(self):
        if not EXACT:
            return f"([r1] {self.a1})"
        if isinstance(self.a1, Lit) or isinstance(self.a1, TRUE_) or isinstance(self.a1, FALSE_):
            return f"(box {self.a1})"
        else:
            return f"(box{self.a1})"

    def write(self, file):
        if isinstance(self.a1, Lit) or isinstance(self.a1, TRUE_) or isinstance(self.a1, FALSE_):
            file.write("([r1] ")
        else:
            file.write("([r1]")
        self.a1.write(file)
        file.write(")")

class Dia(Formula):
    def __init__(self, a1):
        self.a1 = a1

    def __str__(self):
        if not EXACT:
            return f"(<r1> {self.a1})"
        if isinstance(self.a1, Lit) or isinstance(self.a1, TRUE_) or isinstance(self.a1, FALSE_):
            return f"(dia {self.a1})"
        else:
            return f"(dia{self.a1})"
        
    def write(self, file):
        if isinstance(self.a1, Lit) or isinstance(self.a1, TRUE_) or isinstance(self.a1, FALSE_):
            file.write("(<r1> ")
        else:
            file.write("(<r1>")
        self.a1.write(file)
        file.write(")")

done = {}
def p(n):
    global done
    if n not in done:
        done[n] = Lit(n)
    return done[n]

def mbox(n, formula):
    for i in range(n):
        formula = Box(formula)
    return formula

def mdia(n, formula):
    for i in range(n):
        formula = Dia(formula)
    return formula

def list2conj(lst):
    if len(lst) == 0: return TRUE
    cur = lst[0]
    for item in lst[1:]:
        cur = And(cur, item)
    return cur

def list2disj(lst):
    if len(lst) == 0: return FALSE
    cur = lst[0]
    for item in lst[1:]:
        cur = Or(cur, item)
    return cur

from functools import partial

# Infix code from http://tomerfiliba.com/blog/Infix-Operators/
class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def AND(x, y): return And(x, y)
@Infix
def OR(x, y): return Or(x, y)
@Infix
def IMPLIES(x, y): return Implies(x, y)
@Infix
def IFF(x, y): return Iff(x, y)

###############################################################################
def D(p0=p(0)):
    return Box(p0) |IMPLIES| Dia(p0)

def D2(p0=p(0)):
    return Dia(TRUE)

def B(p0=p(0)):
    return p0 |IMPLIES| Box(Dia(p0))

def T(p0=p(0)):
    return Box(p0) |IMPLIES| p0

def A4(p0=p(0)):
    return Box(p0) |IMPLIES| Box(Box(p0))

def A5(p0=p(0)):
    return Not(Box(p0)) |IMPLIES| Box(Not(Box(p0)))

def H(p0=p(0), p1=p(1)):
    return (Box(p0 |OR| p1) |AND| Box(Box(p0) |OR| p1) |AND| Box(p0 |OR| Box(p1))) |IMPLIES| \
        (Box(p0) |OR| Box(p1))

def L(p0=p(0), p1=p(1)):
    return Box(p0 |AND| Box(p0) |IMPLIES| p1) |OR| Box(p1 |AND| Box(p1) |IMPLIES| p0)

def Lplus(p0=p(0), p1=p(1)):
    return Box(Box(p0) |IMPLIES| p1) |OR| Box(Box(p1) |IMPLIES| p0)

def Grz(p0=p(0)):
    return Box(Box(p0 |IMPLIES| Box(p0)) |IMPLIES| p0) |IMPLIES| p0

def Grz1(p0=p(0)):
    return Box(Box(p0 |IMPLIES| Box(p0)) |IMPLIES| p0) |IMPLIES| Box(p0)

def Dum(p0=p(0)):
    return Box(Box(p0 |IMPLIES| Box(p0)) |IMPLIES| p0) |IMPLIES| (Dia(Box(p0)) |IMPLIES| p0)

def Dum1(p0=p(0)):
    return Box(Box(p0 |IMPLIES| Box(p0)) |IMPLIES| p0) |IMPLIES| (Dia(Box(p0)) |IMPLIES| Box(p0))

def Dum4(p0=p(0)):
    return Box(Box(p0 |IMPLIES| Box(p0)) |IMPLIES| p0) |IMPLIES| (Dia(Box(p0)) |IMPLIES| (p0 |OR| Box(p0)))

def nnf(f):
    if isinstance(f, Lit): return f
    if isinstance(f, TRUE_): return f
    if isinstance(f, FALSE_): return f
    if isinstance(f, And): return And(nnf(f.a1), nnf(f.a2))
    if isinstance(f, Or): return Or(nnf(f.a1), nnf(f.a2))
    if isinstance(f, Implies): return nnf(Or(Not(f.a1), f.a2))
    if isinstance(f, Box): return Box(nnf(f.a1))
    if isinstance(f, Dia): return Dia(nnf(f.a1))
    if isinstance(f, Not):
        if isinstance(f.a1, Not):
            return nnf(f.a1.a1)
        if isinstance(f.a1, Box):
            return nnf(Dia(Not(f.a1.a1)))
        if isinstance(f.a1, Dia):
            return nnf(Box(Not(f.a1.a1)))
        if isinstance(f.a1, And):
            return nnf(Or(Not(f.a1.a1), Not(f.a1.a2)))
        if isinstance(f.a1, Or):
            return nnf(And(Not(f.a1.a1), Not(f.a1.a2)))
        if isinstance(f.a1, Implies):
            return nnf(And(f.a1.a1, Not(f.a1.a2)))
        if isinstance(f.a1, Lit):
            return Not(f.a1)
        if isinstance(f.a1, TRUE_): return FALSE
        if isinstance(f.a1, FALSE_): return TRUE
    assert "Missing case in nnf"
    
def size(f):
    if isinstance(f, Lit): return 1
    if isinstance(f, TRUE_): return 1
    if isinstance(f, FALSE_): return 1
    if isinstance(f, And): return 1 + size(f.a1) + size(f.a2)
    if isinstance(f, Or): return 1 + size(f.a1) + size(f.a2)
    if isinstance(f, Implies): return 1 + size(f.a1) + size(f.a2)
    if isinstance(f, Box): return 1 + size(f.a1)
    if isinstance(f, Dia): return 1 + size(f.a1)
    if isinstance(f, Not):return 1 + size(f.a1)
    assert "Missing case in size"

def depth(f):
    if isinstance(f, Lit): return 0
    if isinstance(f, TRUE_): return 0
    if isinstance(f, FALSE_): return 0
    if isinstance(f, And): return max(depth(f.a1), depth(f.a2))
    if isinstance(f, Or): return max(depth(f.a1), depth(f.a2))
    if isinstance(f, Implies): return max(depth(f.a1), depth(f.a2))
    if isinstance(f, Box): return 1 + depth(f.a1)
    if isinstance(f, Dia): return 1 + depth(f.a1)
    if isinstance(f, Not): return depth(f.a1)
    if isinstance(f, Iff): return max(depth(f.a1), depth(f.a2)
)
    assert "Missing case in depth", f

import collections
import functools

# Code from https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__name__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)
