'''
f(x) = exp(-x^2)
a, b = 0, inf.
tsol = sqrt(pi) / 2
'''
import numpy as np

def trapz(F, a, b, n):
	h = (b - a) / float(n)
	summ = 0.5 * (F(a) + F(b))
	for j in range(1, n):
		summ += F(a + j*h)
	return h*summ

def F(x):
	return np.exp(-x**2)

def G(y):
	if (y == 0):
		return 0
	else:
		return np.exp(-1 / y**2) / (y**2)

a, n = 1, 100
tsol = np.sqrt(np.pi) / 2
sol = trapz(F, 0, a, n) + trapz(G, 0, 1/a, n)
err = abs(sol - tsol)
print('sol = ', sol)
print('err = ', err)
