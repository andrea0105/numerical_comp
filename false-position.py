import numpy as np
import matplotlib.pyplot as plt

def func(x):
    f = np.tan(np.pi * x) - 6
    return f

tol = 1.e-10
a, b = 0, 0.48

while True:
    fa = func(a)
    fb = func(b)
    c = (a*fb - b*fa) / (fb - fa)
    print(f'a = {a}, b = {b}, c = {c}, |c - a| = {abs(c-a)}')
    if abs(c - a) < tol:
        break
    if fa * func(c) < 0:
        b = c
    else:
        a = c

print(c, func(c))
