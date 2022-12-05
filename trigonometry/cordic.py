from cmath import cos, sin
import numpy as np

_beta_ = np.deg2rad(23.7)

def cordic(beta):
    n = 100
    x = np.array([1., 0.])
    #gamma = np.arctan(2.**(-np.arange(n)))
    for i in range(n):
        gamma = np.arctan(2.**(-i))
        if beta < 0:
            sigma = -1
        else:
            sigma = 1
        beta -= sigma * gamma
        factor = sigma * 2.**(-i)
        R = np.array([[1., -factor], [factor, 1.]])
        R = R / np.sqrt(1+factor**2)
        x = R @ x
    return x

x = cordic(_beta_)
cosine = np.cos(_beta_)
sine = np.sin(_beta_)
print(f'Results from CORDIC: cos={x[0]}, sin={x[1]}')
print(f'numpy cos={cosine}, sin={sine}')

Err1 = x[0] - cosine
Err2 = x[1] - sine
print(f'Error: cos={np.abs(Err1)}, sin={np.abs(Err2)}')