import numpy as np

e = 0.9

def f(y, x):
    f = y - e * np.sin(y) - x
    df = 1 - e * np.cos(y)
    return f, df

x = np.linspace(0, np.pi, 30)
y = 1
tol = 1.e-12
roots = []

for i in range(len(x)):
    while True:
        f0, df = f(y, x[i])
        ratio = f0 / df
        if np.abs(ratio) < tol:
            roots.append(y)
            break
        else:
            y -= ratio

print(roots)
print(len(roots))
