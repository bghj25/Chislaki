import numpy as np
import matplotlib.pyplot as plt
a = 0
b = 5
n = int(input())
h = (b - a)/n

x_arr = np.linspace(a - (b - a) / (n - 1), b + (b - a) / (n - 1), n + 2)
#print(x_arr)
y_arr = x_arr ** 2 / 2
x_arr_to_plot = np.delete(x_arr, [0, len(x_arr) - 1])
y_arr_to_plot = np.delete(y_arr, [0, len(y_arr) - 1])

y_arr_dif = []
for i in range(1, n + 1):
    y_arr_dif.append((y_arr[i + 1] - y_arr[i]) / h)

fig = plt.figure()
fig.suptitle('Первая производная, правые разности')
plt.plot(x_arr_to_plot, y_arr_to_plot)
plt.plot(x_arr_to_plot, y_arr_dif)

y_arr_dif = []
for i in range(1, n + 1):
    y_arr_dif.append((y_arr[i + 1] - y_arr[i - 1])/(2 * h))

fig = plt.figure()
fig.suptitle('Первая производная, центральные разности')
plt.plot(x_arr_to_plot, y_arr_to_plot)
plt.plot(x_arr_to_plot, y_arr_dif)

plt.show()

