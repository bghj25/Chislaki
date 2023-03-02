import numpy as np
import matplotlib.pyplot as plt
a = 0
b = 5
n = int(input())
h = (b - a)/n

x_arr = np.linspace(a - 2 * (b - a) / (n - 1), b + 2 * (b - a) / (n - 1), n + 4)
#print(x_arr)
y_arr = x_arr ** 3
x_arr_to_plot = np.delete(x_arr, [0, 1, len(x_arr) - 1, len(x_arr) - 2])
y_arr_to_plot = np.delete(y_arr, [0, 1, len(y_arr) - 1, len(y_arr) - 2])

y_arr_derivative = []
for i in range(2, n + 2):
    y_arr_derivative.append((y_arr[i + 1] - y_arr[i]) / h)

fig = plt.figure()
fig.suptitle('Первая производная, правые разности')
plt.plot(x_arr_to_plot, y_arr_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)

y_arr_derivative = []
for i in range(2, n + 2):
    y_arr_derivative.append((y_arr[i + 1] - y_arr[i - 1])/(2 * h))

fig = plt.figure()
fig.suptitle('Первая производная, центральные разности')
plt.plot(x_arr_to_plot, y_arr_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)

y_arr_derivative = []
for i in range(2, n + 2):
    y_arr_derivative.append((y_arr[i + 1] - 2 * y_arr[i] + y_arr[i - 1])/(h ** 2))

fig = plt.figure()
fig.suptitle('Вторая производная, второй порядок точности')
plt.plot(x_arr_to_plot, y_arr_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)


y_arr_derivative = []
print(y_arr_to_plot)
for i in range(2, n + 2):
    y_arr_derivative.append((-y_arr[i + 2] + 16 * y_arr[i + 1] * y_arr[i] - 30 * y_arr[i] +
                             16 * y_arr[i - 1] - y_arr[i - 2])/(h ** 4))

fig = plt.figure()
fig.suptitle('Вторая производная, четвертый порядок точности')
plt.plot(x_arr_to_plot, y_arr_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)

plt.show()

