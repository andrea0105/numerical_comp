import numpy as np
import matplotlib.pyplot as plt

def func(x):
    f = x**4 - 3*x - 1
    df = 4*x**3 - 3
    return f, df

x, count = 1, 0
tol = 1.e-12

while True:
    f0, df = func(x)
    ratio = f0 / df
    print(f'x = {x:.5f} f(x) = {f0:.5e} ratio = {ratio:.5e}')
    if abs(ratio) < tol:
        break
    x -= ratio

print(f'Final x = {x}')

n = np.linspace(-3, 3, 10000)
results = np.ones(len(n))
results_df = np.ones(len(n))
for i in range(len(n)):
    results[i], results_df[i] = func(n[i])

plt.figure(1, figsize=(10, 5))
plt.plot(n, results)
plt.grid('on')
plt.show()
