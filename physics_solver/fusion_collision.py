"""
The collision cross-sectional area of Particles in Nuclear-Fusion.
Author: Jaewhan Lee
"""
import numpy as np
import matplotlib.pyplot as plt

V = 0.1
coef = [1/25, (2/5)*np.log(V), (np.log(V)**2), -2]
dcoef = np.polyder(coef)
deg = len(coef) - 1

tol = 1.e-10
roots = []
for k in range(deg):
    E = 1.0
    while True:
        dlng = complex(0, 1.e-20)
        for r in roots:
            dlng += 1 / (E - r)
        Vx = np.polyval(coef, E)
        dVx = np.polyval(dcoef, E)
        err = Vx / (dVx - Vx*dlng)
        if np.abs(err) < tol:
            break
        E = E - err
    roots.append(E)

print(np.sort_complex(roots))
