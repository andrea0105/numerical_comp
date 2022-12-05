import numpy as np
from scipy import integrate

def func(x):
	return np.sin(x)

def trapz(F, a, b, n):
	h = (b - a) / float(n)
	summ = 0.5 * (F(a) + F(b))
	for j in range(1, n):
		summ += F(a + j*h)
	return h*summ

def romberg(F, a, b, n):
	Jmax = 10
	T = np.zeros((Jmax, Jmax), dtype=float)
	T[0, 0] = (b - a) * (F(a) + F(b))
	for j in range(1, Jmax):
		T[j, 0] = trapz(func, a, b, 2**j)
		for k in range(1, j+1):
			T[j, k] = T[j, k-1] + (T[j, k-1] - T[j-1, k-1])/(4**k - 1.0)
		if (abs(T[j, j] - T[j-1 ,j-1]) < tol):
			break
	return T[j, j]

a, b = 0, np.pi
tol = 1.e-8
sol = romberg(func, a, b, tol)
err = abs(sol - 2)
print(sol, err)

a, b = 0., np.pi
sol = integrate.romberg(func, a, b, tol=1.e-10, show=True)
print(sol)
