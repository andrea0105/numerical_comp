import numpy as np
import cmath

def func(x):
    return x**4 - 3*x - 1

x0, x1, x2 = -1.0, 0.0, 2.0
tol = 1.e-10
while True:
    f0 = func(x0)
    f1 = func(x1)
    f2 = func(x2)
    F10 = (f1 - f0) / (x1 - x0)
    F210 = ((f2 - f1) / (x2 - x1) - F10) / (x2 - x0)
    a = F210
    b = F10 + F210*(x0 - x1)
    c = f0
    xp = x0 - (2*c / (b + cmath.sqrt(b**2 - 4*a*c)))
    xm = x0 - (2*c / (b - cmath.sqrt(b**2 - 4*a*c)))
    if abs(func(xm)) < abs(func(xp)):
        xnew = xm
    else:
        xnew = xp
    if abs(xnew - x1) < tol:
        break
    x0 = x1
    x1 = x2
    x2 = xnew

print(f'solution = {xnew}   func(x) = {func(xnew)}')
