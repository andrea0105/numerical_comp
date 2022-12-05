import numpy as np

x1 = 10
x2 = -10
r = np.linspace(0, np.log10(2)/2, 10000)
n = np.linspace(0, 30, 10000)

# The way how compute exp funtion by using log10 function

def find(x1):
    x = 0
    for i in range(len(n)):
        for j in range(len(r)):
            x = n[i] * np.log10(2) + r[j]
            if np.abs(x - x1) <= 1e-15:
                return n[i], r[j]
            else:
                continue

x = find(x1)
print(x)
