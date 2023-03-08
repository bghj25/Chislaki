import numpy as np
import matplotlib.pyplot as plt


def L(n, i, x_ar, x):
    l = 1
    for k in range(n):
        if k != i:
            l *= (x - x_ar[2 * k]) / (x_ar[2 * i] - x_ar[2 * k])
    return l


n1 = int(input())
x_arr = np.linspace(0, 10, num=2 * n1 - 1)
y_arr = np.sinh((np.sin(x_arr / 5)) ** 2)
#plt.axvline(x = x_arr, ymin = 0, ymax = 1, alpha = 0.1)
plt.plot(x_arr, y_arr)
y_arr_interp = []
for x in x_arr:
    y = 0
    for i in range(n1):
        y += y_arr[2 * i] * L(n1, i, x_arr, x)
    y_arr_interp.append(y)
plt.plot(x_arr, y_arr_interp)
plt.show()
RMSD = 0
for i in range(1, 2 * n1 - 1, 2): #СКО считаем только в точках лежащих между "заданными"
    RMSD += (y_arr_interp[i] - y_arr[i]) ** 2
RMSD /= (2 * n1 - 1)
print(RMSD)

