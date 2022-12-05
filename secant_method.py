import numpy as np

def func(x):
    f = x**4 - 3*x - 1
    return f

tol = 1.e-6
x0, x1 = 1, 2   #반드시 근을 둘러쌀 필요는 없지만 근을 못구하는 경우가 있다
while True:
    f0 = func(x0)
    f1 = func(x1)
    x2 = x1 - f1*(x1 - x0)/(f1 - f0)
    print(f'{x2:.5f}    {func(x2):.5e}  {abs(x2-x1):.5e}')
    if abs(x2-x1) < tol:
        break
    else:
        x0 = x1     #순서가 바뀌지 않게 주의
        x1 = x2
print(x2)
