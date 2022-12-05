'''
The Planck Function describes a radiation from a blackbody with a temperature, T.
B(T) = (2hc^2 / lambda^5) / [exp(hc/(lambda*Kb*T)) - 1]
Solve this equation to find the relationship between T and lambda
(x-5)e^x + 5 = 0
Wien's displacement law
x = hc / Kb*T*lambda
For computation, newton-raphson method is utillzed.
'''
import numpy as np

h = 6.626e-34       # J*s
Kb = 1.381e-23      # J*k^-1
c = 2.998e+8        # m*s^-1
B = 1.e+13          # J*s^-1*m*-3
T = 1.e+4           # K

a = (h * c) / (Kb * T)
coef = [a, 0.5*a**2, (1/6)*a**3, 0, -(h*c**2)/B]
dcoef = np.polyder(coef)
deg = len(coef) - 1
tol = 1.e-12
roots = []
for k in range(deg):
    x = 1.0
    while True:
        dlng = complex(0, 1.e-20)
        for r in roots:
            dlng += 1 / (x - r)
        fx = np.polyval(coef, x)
        dfx = np.polyval(dcoef, x)
        err = fx / (dfx - fx*dlng)
        if np.abs(err) < tol:
            break
        x = x - err
    roots.append(x)
print(np.sort_complex(roots))

def wien(x):
    f = (x - 5)*np.exp(x) + 5
    df = (x - 4)*np.exp(x)
    return f, df

T_lam0 = 0.001
x0 = (h * c) / (Kb * T_lam0)
tol = 1.e-12

while True:
    f, df = wien(x0)
    ratio = f / df
    if abs(ratio) < tol:
        break
    else:
        x0 -= ratio

print(f'T*lambda = {h*c/(Kb*x0)}')
