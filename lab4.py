import numpy as np


def function(x_):
    return np.cosh(1 / (1 + x_)) - np.tanh(x_) - x_


def derivative(x_):
    return -np.sinh(1 / (1 + x_)) / (x_ ** 2 + 2 * x_ + 1) - 1 / (np.cosh(x_) ** 2) - 1


a = 0
b = 10
eps = b - a
flag1 = True
flag2 = True
c = 0
f_a = 0
f_b = 0
f_c = 0
iterations = 0
print('bisection')
while eps > 1e-9:
    c = (b + a) / 2
    f_a = function(a)
    f_b = function(b)
    f_c = function(c)
    if f_c == 0:
        print('Точное решение', c)
        break
    elif f_a * f_c < 0:
        b = c
    else:
        a = c
    eps = b - a
    iterations += 1
    if (eps < 0.001) and flag1:
        print('eps = ', eps, ', x* = ', c, ', f(x*) = ', f_c, ', iters = ', iterations)
        flag1 = False
    if (eps < 1e-6) and flag2:
        print('eps = ', eps, ', x* = ', c, ', f(x*) = ', f_c, ', iters = ', iterations)
        flag2 = False

print('eps = ', eps, ', x* = ', c, ', f(x*) = ', f_c, ', iters = ', iterations)



eps = 1
flag1 = True
flag2 = True
x = np.array([10])

iterations = 0
print('newton')
while eps > 1e-9:
    x = np.append(x, x[len(x) - 1] - function(x[len(x) - 1]) / derivative(x[len(x) - 1]))
    eps = np.abs(x[len(x) - 1] - x[len(x) - 2])
    iterations += 1
    if (eps < 0.001) and flag1:
        print('eps = ', eps, ', x* = ', x[len(x) - 1], ', f(x*) = ', function(x[len(x) - 1]), ', iters = ', iterations)
        flag1 = False
    if (eps < 1e-6) and flag2:
        print('eps = ', eps, ', x* = ', x[len(x) - 1], ', f(x*) = ', function(x[len(x) - 1]), ', iters = ', iterations)
        flag2 = False
print('eps = ', eps, ', x* = ', x[len(x) - 1], ', f(x*) = ', function(x[len(x) - 1]), ', iters = ', iterations)