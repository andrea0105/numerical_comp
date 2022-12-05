import numpy as np
import matplotlib.pyplot as plt

'''
Temperature is T, non-dimensional magnetism of ferromagnetic body. (M > 0)

M = tanh(M / T)
0 < T <= 2
'''
Temp = np.linspace(1.e-12, 2, 100)
tol = 1.e-12
roots = []
result = []

for T in Temp:
    coef = [(17/(315*T**7)), 0, (-2/(15*T**5)), 0, (1/(3*T**3)), 0, (1 - (1/T))]
    dcoef = np.polyder(coef)
    deg = len(coef) - 1
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
        roots.append(x.real)
    result.append(roots[2])

plt.plot(Temp, result)
plt.show()
