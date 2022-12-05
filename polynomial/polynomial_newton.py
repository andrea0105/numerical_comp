import numpy as np
coef = [1, 0, 0, 0, 0, -3, -1]
dcoef = np.polyder(coef)
deg = len(coef) - 1

tol = 1.e-10
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
