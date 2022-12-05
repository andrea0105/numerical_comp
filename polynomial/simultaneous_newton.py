import numpy as np
from scipy import linalg
from scipy.optimize import fsolve
import cmath

def func(x):
    f = [ x[0]*np.cos(x[1]) - 4, (x[0] - 1)*x[1] - 5 ]
    return f

def Jacobi(x):
    j = [ [np.cos(x[1]), -x[0]*np.sin(x[1])], \
            [x[1], x[0] - 1] ]
    return j

x = [5, 0]
tol = 1.e-10

while True:
    j = Jacobi(x)
    f = func(x)
    J_inv  = linalg.inv(j)
    err = J_inv @ f
    if linalg.norm(err) < tol:
        break
    x = x - err

print(x)

def func2(x):
    return [x[0]*np.cos(x[1]) - 4, (x[0] - 1)*x[1] - 5]

roots = fsolve(func2, [1, 1], xtol=1.e-10)
print(roots)

def func3(x):       #로그나 루트가 있을땐 cmath모듈을 이용한다.
    f1 = np.abs(x[0]**2 + cmath.sqrt(1 - x[1]) - 3) #실수값을 가져야한다!
    f2 = np.abs(cmath.log(x[0]) + x[1] + 2) #np.abs로 실수값을 갖도록 한다.
    return [f1, f2]

roots = fsolve(func3, [1, 2], xtol=1.e-10)
print(roots)
