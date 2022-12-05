import numpy as np

def gfunc(x):
    g = (3*x + 1)**0.25
    return g

tol = 1.e-6
x0 = 1

while True:
    x1 = gfunc(x0)
    if abs(x1 - x0) < tol:
        break
    x0 = x1

print(x1)
