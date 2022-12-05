import numpy as np
import matplotlib.pyplot as plt

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def exp(x):
    iter = 1000
    c, _sum_ = 0, 0
    for n in range(0, iter, 1):
        xp = float((x**n) / factorial(n))- c
        sp = _sum_
        _sum_ += xp
        c = ((sp + xp) - sp) - xp
    return _sum_

def double_prime(x, h):
    number = np.ones(len(h))
    for i in range(len(h)):
        step = h[i]
        A = -(x + step)**2
        B = -(x**2)
        C = -(x - step)**2
        number[i] = (np.exp(A) - 2*np.exp(B) + np.exp(C)) / (step**2)
    return number

h = np.logspace(-5, 1, 10000)
results = double_prime(1, h)
real_solution =  2 * np.exp(-1)
Error = np.abs(results - real_solution)

plt.figure(1, figsize=(10, 5))
plt.xlabel('$Step size$')
plt.ylabel('$Error$')
plt.xscale('log')
plt.plot(h, Error,'k', label='Error')
plt.legend()
plt.show()
