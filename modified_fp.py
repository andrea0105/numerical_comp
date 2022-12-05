import numpy as np

def func(x):
    f = np.tan(np.pi*x) - 6
    return f

tol = 1.e-10
a, b = 0, 0.48

pfc = 0
fa = func(a)
fb = func(b)
while True:
    c = (a*fb - b*fa) / (fb - fa)
    print(f'a = {a:.5f} b = {b:.5f}  c = {c:.5f}')
    if abs(a - c) < tol:
        break
    fc = func(c)
    if fa*fc < 0:
        b = c
        fb = func(b)
        if fc*pfc > 0:
            fa = 0.5 * fa
    else:
        a = c
        fa = func(a)
        if fc*pfc > 0:
            fb = 0.5 * fb
    pfc = fc

print(c, func(c)
