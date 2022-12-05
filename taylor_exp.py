import numpy as np

x1 = 10
x2 = -10
sol1 = np.exp(x1)
sol2 = np.exp(x2)

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def exp(x):
    _sum_ = 0
    iter = 1000
    n_factorial = 1
    c, _sum_ = 0, 0
    for n in range(0, iter, 1):
        xp = ((x**n) / factorial(n)) - c
        sp = _sum_
        if np.abs(xp) <= 10**(-8):
            continue
        else:
            _sum_ += xp
        c = ((sp + xp) - sp) - xp
    return _sum_

print(f'taylor series when x = 10: {exp(x1)}')
print(f'numpy exp when x = 10: {sol1}')
print(f'taylor series when x = -10: {exp(x2)}')
print(f'numpy exp when x = -10: {sol2}')
print(f'Error when x = 10: {exp(x1) - sol1}')
print(f'Error when x = -10: {exp(x2) - sol2}')
