import numpy as np

def func(x):
    f = x**4 - 3*x - 1
    return f

tol = 1.e-6     #Error tolerance
a, b = 1, 2     #Initial range

while True:
    fa = func(a)
    fb = func(b)
    c = 0.5 * (a + b)
    fc = func(c)
    print(f'a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, |a-c| = {abs(a-c):.4f}, f(c) = {fc:.4f}')
    if np.abs(a-c) < tol:
        solution = c
        break
    if fa*fc < 0.:
        b = c
    else:
        a = c

print(solution)
