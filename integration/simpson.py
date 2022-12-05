import numpy as np
from scipy import integrate

def func(x):
	return np.exp(x)

def simpson(F, a, b, n):
	h = (b - a) / float(n)
	summ = F(a) + F(b)
	for j in range(1, n-1, 2):
		summ += 4.*F(a + j*h)
		summ += 2.*F(a + (j + 1)*h)
	summ += 4.*F(b - h)
	return summ*(h/3)

a, b = 0., 1.
perr = 1.
for i in range(1, 10):
	n = 2**i
	sol = simpson(func, a, b, n)
	err = abs(np.exp(1) - 1 - sol)
	ratio = perr / err
	perr = err
	print(f'{n:3d}	{sol:.6f}	{err:.4e}	{ratio:.2f}')

a, b = 0., 1.
for j in range(10):
	n = 2**j
	x = np.linspace(a, b, n+1)
	y = func(x)
	sol = integrate.simps(y, x)
	err = abs(np.exp(1) - 1 - sol)
	print(f'sol = {sol}		err = {err}')
