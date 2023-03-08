import numpy as np
import matplotlib.pyplot as plt


def mse(arr1, arr2, n_):
    return np.sum((arr1 - arr2) ** 2 / n_)


def der_1_right(y_arr_, n_, h_):
    y_arr_derivative_ = []
    for i in range(n_ - 1):
        y_arr_derivative_.append((y_arr_[i + 1] - y_arr_[i]) / h_)
    return y_arr_derivative_


def der_1_central(y_arr_, n_, h_):
    y_arr_derivative_ = []
    for i in range(1, n_ - 1):
        y_arr_derivative_.append((y_arr_[i + 1] - y_arr_[i - 1]) / (2 * h_))
    return y_arr_derivative_


def der_2_ord2(y_arr_, n_, h_):
    y_arr_derivative_ = []
    for i in range(1, n_ - 1):
        y_arr_derivative_.append((y_arr_[i + 1] - 2 * y_arr_[i] + y_arr_[i - 1]) / h_**2)
    return y_arr_derivative_


def der_2_ord4(y_arr_, n_, h_):
    y_arr_derivative_ = []
    for i in range(2, n_ - 2):
        y_arr_derivative_.append((-y_arr_[i + 2] + 16 * y_arr_[i + 1] - 30 * y_arr_[i] +
                                 16 * y_arr_[i - 1] - y_arr_[i - 2])/(12 * h_**2))
    return y_arr_derivative_


a = -1.5
b = 1.5
n = int(input())
h = (b - a)/n
x_arr = np.linspace(a, b, n)
y_arr = x_arr / (1 + (np.tan(x_arr)) ** 2)
y_arr_analytic = ((np.cos(x_arr)*np.tan(x_arr))**2 - 2*x_arr*np.tan(x_arr) + (np.cos(x_arr))**2) / \
                 (np.cos(x_arr)*((np.tan(x_arr))**2+1))**2

t = np.tan(x_arr)
s = 1 / (np.cos(x_arr))
zn = 1 + t ** 2
d1 = 8 * x_arr * t**2 * s**4 / zn**3
d2 = -2 * x_arr * s**4 / zn**2
d3 = -4 * x_arr * t**2 * s**2 / zn**2
d4 = -4 * t * s**2 / zn**2
y_arr_analytic_2nd = d1 + d2 + d3 + d4

fig = plt.figure()
y_arr_derivative = der_1_right(y_arr, n, h)
x_arr_to_plot = np.delete(x_arr, n - 1)
y_arr_analytic_to_plot = np.delete(y_arr_analytic, n - 1)
plt.plot(x_arr_to_plot, y_arr_analytic_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)
fig.suptitle('Первая производная, правые разности \n СКО = ' +
             str(mse(y_arr_analytic_to_plot, y_arr_derivative, len(y_arr_derivative))))

fig = plt.figure()
y_arr_derivative = der_1_central(y_arr, n, h)
x_arr_to_plot = np.delete(x_arr, [0, n - 1])
y_arr_analytic_to_plot = np.delete(y_arr_analytic, [0, n - 1])
plt.plot(x_arr_to_plot, y_arr_analytic_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)
fig.suptitle('Первая производная, центральные разности \n СКО = ' +
             str(mse(y_arr_analytic_to_plot, y_arr_derivative, len(y_arr_derivative))))

fig = plt.figure()
y_arr_derivative = der_2_ord2(y_arr, n, h)
x_arr_to_plot = np.delete(x_arr, [0, n - 1])
y_arr_analytic_to_plot = np.delete(y_arr_analytic_2nd, [0, n - 1])
plt.plot(x_arr_to_plot, y_arr_analytic_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)
fig.suptitle('Вторая производная, второй порядок точности \n СКО = ' +
             str(mse(y_arr_analytic_to_plot, y_arr_derivative, len(y_arr_derivative))))

fig = plt.figure()
y_arr_derivative = der_2_ord4(y_arr, n, h)
x_arr_to_plot = np.delete(x_arr, [0, 1, n - 2, n - 1])
y_arr_analytic_to_plot = np.delete(y_arr_analytic_2nd, [0, 1, n - 2, n - 1])
print(x_arr_to_plot)
print(y_arr_derivative)
plt.plot(x_arr_to_plot, y_arr_analytic_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)
fig.suptitle('Вторая производная, четвертый порядок точности \n СКО = ' +
             str(mse(y_arr_analytic_to_plot, y_arr_derivative, len(y_arr_derivative))))

plt.show()
