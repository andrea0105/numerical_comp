import numpy as np
import cmath

def muller(p, x0, x1, x2, tol):
    deg = len(p) - 1
    while True:
        f0 = np.polyval(p, x0)
        f1 = np.polyval(p, x1)
        f2 = np.polyval(p, x2)
        F10 = (f1 - f0) / (x1 - x0)
        F210 = ((f2 - f1) / (x2 - x1) - F10) / (x2 - x0)
        a = F210
        b = F10 + F210*(x0 - x1)
        c = f0
        xp = x0 - (2*c / (b + cmath.sqrt(b**2 - 4*a*c)))
        xm = x0 - (2*c / (b - cmath.sqrt(b**2 - 4*a*c)))
        if abs(np.polyval(p, xm)) < abs(np.polyval(p, xp)):
            xnew = xm
        else:
            xnew = xp
        if np.abs(np.polyval(p, xnew)) < tol:
            break
        x2, x1, x0 = x1, x0, xnew
    return xnew

a = [1, 0, 0, 0, 0, -3, -1]     #x^6 - 3x - 1 = 0
deg = len(a) - 1                #다항식의 차수 계산

tol = 1.e-10
roots = []
x0, x1, x2 = 1, 2, 3                        #처음 3개의 점
for k in range(deg - 2):                    #수축다항식이 2차 다항식이 될 때까지
    sol = muller(a, x0, x1, x2, tol)
    roots.append(sol)
    b = np.zeros(len(a) - 1, dtype=complex) #수축다항식의 계수 b를 초기화
    b[0] = a[0]
    for i in range(1, len(b)):
        b[i] = a[i] + sol*b[i - 1]      #수축다항식의 계수 관계
    a = b       #계수 b를 계수 a로 바꾸고 계산을 반복한다

solp = (-b[1] + cmath.sqrt(b[1]**2 - 4*b[0]*b[2])) / (2*b[0])
solm = (-b[1] - cmath.sqrt(b[1]**2 - 4*b[0]*b[2])) / (2*b[0])
roots.extend([solp, solm])
print(np.sort_complex(roots))
