import numpy as np

n = 10**8

def kahan(n):
    c, _sum_ = 0, 0
    for i in range(1, n+1, 1):
        xp = (i*(i+2))**(-1) - c
        sp = _sum_
        _sum_ += xp
        c = ((sp+xp)-sp)-xp
    return _sum_

def from_small(n):
    _sum_ = 0
    for i in range(1, n+1, 1):
        _sum_ += (i*(i+2))**(-1)
    return _sum_

def from_big(n):
    _sum_ = 0
    for i in range(n, 0, -1):
        _sum_ += (i*(i+2))**(-1)
    return _sum_

real_val = (n*(3*n+5)) / (4*(n+1)*(n+2))
print(f'Real Value: {real_val}')

Err1 = kahan(n) - real_val
Err2 = from_small(n) - real_val
Err3 = from_big(n) - real_val

print(f'Kahan Error: {Err1}')
print(f'From small to large Error: {Err2}')
print(f'From big to small Error: {Err3}')
