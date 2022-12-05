import numpy as np

a10 = 46189/256
a9 = 0
a8 = -109395/256
a7 = 0
a6 = 90090/256
a5 = 0
a4 = -30030/256
a3 = 0
a2 = 3456/256
a1 = 0
a0 = -63/256

coef = [a10, a9, a8, a7, a6, a5, a4, a3, a2, a1, a0]
dcoef = np.polyder(coef)
deg = len(coef) - 1
tol = 1.e-12
roots = []

for i in range(deg):
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
