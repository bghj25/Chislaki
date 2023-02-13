import numpy as np
import matplotlib.pyplot as plt


def L(n, i, x_ar, x):
    l = 1
    for k in range(n):
        if k != i:
            l *= (x - x_ar[k]) / (x_ar[i] - x_ar[k])
    return l


n1 = int(input())
x_cheb = []

for k in range(n1):
    x_k = (0 + 10)/2 + (10-0)/2 * np.cos((2*(k+1)-1) * np.pi / (2*n1))
    x_cheb.append(x_k)
x_cheb = np.array(x_cheb)
y_arr = np.sinh((np.sin(x_cheb / 5)) ** 2)
y_arr_interp = []
for x in x_cheb:
    y = 0
    for i in range(n1):
        y += y_arr[i] * L(n1, i, x_cheb, x)
    y_arr_interp.append(y)
plt.plot(x_cheb, y_arr_interp)

x_arr = np.linspace(0, 10, num=2 * n1)
y_arr = np.sinh((np.sin(x_arr / 5)) ** 2)
plt.plot(x_arr, y_arr)
plt.show()
