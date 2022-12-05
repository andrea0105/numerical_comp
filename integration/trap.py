import numpy as np
from scipy import integrate

def func(x):
	return np.exp(x)

def trap(F, a, b, n):
	h = (b - a) / float(n)
	summ = 0.5 * (F(a) + F(b))
	for j in range(1, n):
		summ += F(a + j*h)
	return h*summ

a, b = 0., 1.
perr = 1.
for i in range(0, 10):
	n = 2**i
	sol = trap(func, a, b, n)
	err = abs(np.exp(1) - 1 - sol)
	ratio = perr / err
	perr = err
	print(f'{n:3d}	{sol:.6f}	{err:.4e}	{ratio:.2f}')

a, b = 0., 1.
for j in range(10):
	n = 2**j
	x = np.linspace(a, b, n+1)
	y = func(x)
	sol = integrate.trapz(y, x)
	err = abs(np.exp(1) - 1 - sol)
	print(f'sol={sol:.6e}	err={err:.6e}')
