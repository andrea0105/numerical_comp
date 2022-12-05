import numpy as np
from scipy import linalg
from scipy.optimize import fsolve
import cmath

def func(x):
    f = [2*x[0] + x[1] - x[0]*x[1] + 5, 2*x[0]*np.exp(-x[1]) - 1]
    return f

def jacobi(x):
    j = [[2 - x[1], 1 - x[0]], [2*np.exp(-x[1]), -2*x[0]*np.exp(-x[1])]]
    return j

x = [4, 0]
tol = 1.e-12

while True:
    j = jacobi(x)
    f = func(x)
    j_inv = linalg.inv(j)
    err = j_inv @ f
    if linalg.norm(err) < tol:
        break
    x = x - err

print(x)
