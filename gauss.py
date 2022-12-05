'''
f(x) = 1 / (1 + x^2)
a, b = -1, 1

Analytic Solution = 2arctan(1)

Varying the number of nodes from n = 1,2,4,8,16
Compare the error from each numbers
'''
import numpy as np

func = lambda x: 1 / (1 + x**2)
tsol = 2 * np.arctan(1)
for i in range(5):
	n = 2**i
	x, w = np.polynomial.legendre.leggauss(n)	# Finding nodes and weights
	gauss = np.sum(w * func(x))
	err = abs(gauss - tsol)
	print(f'n={n:2d}	sum={gauss:.7e}	err={err:.7e}')
print("------------------------------------------")
'''
Above integration only works over [-1, 1]

Substitute the variable to integrate over [a, b]

f(x) = 1 / (2 + cos(x))
a, b = 0, 2pi
tsol = 2pi / sqrt(3)
Change the number of nodes from n=1, 2, --- , 2^5, 2^6
'''
f = lambda x: 1 / (2 + np.cos(x))
tsol = 2*np.pi / np.sqrt(3)

a, b = 0, 2*np.pi
for i in range(7):
	n = 2**i
	t, w = np.polynomial.legendre.leggauss(n)
	x = 0.5 *(b + a + t*(b -  a))
	gauss = 0.5 * (b - a) * np.sum(w * f(x))
	err = abs(gauss - tsol)
	print(f'n={n:2d}	sum={gauss:.5e}	err={err:.5e}')
print("------------------------------------------")
'''
scipy.integrate.quadrature() follows gauss-quadrature integration
'''
from scipy import integrate

f2 = lambda x: 1 / (2 + np.cos(x))

a, b = 0., 2*np.pi
val, err = integrate.quadrature(f2, a, b, tol=1.e-10)
print(val, err)
