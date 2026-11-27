from fractions import Fraction
from itertools import permutations
from math import comb, exp, factorial

def included(p):
    m = len(p)//2
    return any(p[2*i]//2 == p[2*i+1]//2 < m for i in range(m))

def family_size(n):
    return sum((-1)**(k+1)*comb(n//2,k)**2*factorial(k)*2**k*factorial(n-2*k)
               for k in range(1,n//2+1))

for n in range(4,10):
    brute = sum(included(p) for p in permutations(range(n)))
    assert brute == family_size(n)
    print(n, brute, float(Fraction(brute,factorial(n))))
for n in (20, 50, 100, 501):
    print(n, float(Fraction(family_size(n),factorial(n))))
print("limit",1-exp(-.5))

# The 4 x 4 visual fixes the pair involution and tests all 24 transversals.
mates = {(r, c): (r ^ 1, c ^ 1) for r in range(4) for c in range(4)}
assert all(mates[mates[cell]] == cell for cell in mates)
values = []
for columns in permutations(range(4)):
    transversal = set(enumerate(columns))
    pairs = [(cell, mate) for cell, mate in mates.items()
             if cell < mate and {cell, mate} <= transversal]
    assert bool(pairs) == included(columns)
    values.append(len(pairs))
    for cell, mate in pairs:
        assert mates[cell] == mate and all(x != y for x, y in zip(cell, mate))
assert values.count(0) == 16 and values.count(1) == 0 and values.count(2) == 8
print("4 x 4 explorer: 16 transversals without paired cells, eight with two complete pairs.")
