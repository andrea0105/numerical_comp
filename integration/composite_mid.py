'''
Using Composite midpoint rule.
f = sinx
T: 0 <= T <= pi
I = 2
n = 1, 2, 2^2, 2^3, ..., 2^10
Calculate how much errors are lowered down by dubling n. 
합성 중점법칙을 이용하여 I를 계산하고,
n이 위와 같이 증가되면서 오차가 몇 배씩 감소하는지 확인.
'''
import numpy as np

def func(x):
    return np.sin(x)

def midpoint(F, a, b, n):
    summ = 0
    h = (b - a) / float(n)
    for j in range(n):
        c = a + (0.5 + j)*h # Xj + Xj+1 / 2 -> midpoint
        summ += F(c)
    return h*summ

a, b = 0, np.pi # 적분 구간
perr = 1
for i in range(0, 10, 1):
    n = 2**i
    sol = midpoint(func, a, b, n) # 함수를 매개변수로 전달!
    err = abs(2.0 - sol)    # 해석해인 2와 수치해를 비교
    ratio = perr / err
    perr = err
    print(f'{n:3d}  {sol:.6f}   {err:.4e}   {ratio:.2f}')
print('n이 2배 증가할 때 마다 오차가 4배씩 줄어든다. 따라서 2차의 정확도')
