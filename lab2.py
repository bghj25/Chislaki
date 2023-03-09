import numpy as np
import matplotlib.pyplot as plt


def mse(arr1, arr2, n_):
    return np.sum((arr1 - arr2) ** 2 / n_)


def function(x_arr_):
    return x_arr_ / (1 + (np.tan(x_arr_)) ** 2)


def der_1_analytic(x_arr_):
    return ((np.cos(x_arr_) * np.tan(x_arr_)) ** 2 - 2 * x_arr_ * np.tan(x_arr_) + (np.cos(x_arr_)) ** 2) / \
                 (np.cos(x_arr_) * ((np.tan(x_arr_)) ** 2 + 1)) ** 2


def der_2_analytic(x_arr_):
    t = np.tan(x_arr_)
    s = 1 / (np.cos(x_arr_))
    zn = 1 + t ** 2
    d1 = 8 * x_arr_ * t ** 2 * s ** 4 / zn ** 3
    d2 = -2 * x_arr_ * s ** 4 / zn ** 2
    d3 = -4 * x_arr_ * t ** 2 * s ** 2 / zn ** 2
    d4 = -4 * t * s ** 2 / zn ** 2
    return d1 + d2 + d3 + d4


def der_1_right(y_arr_, n_, h_):
    y_arr_derivative_ = np.array([])
    for i_ in range(n_ - 1):
        y_arr_derivative_ = np.append(y_arr_derivative_, (y_arr_[i_ + 1] - y_arr_[i_]) / h_)
    return y_arr_derivative_


def der_1_central(y_arr_, n_, h_):
    y_arr_derivative_ = np.array([])
    for i_ in range(1, n_ - 1):
        y_arr_derivative_ = np.append(y_arr_derivative_, (y_arr_[i_ + 1] - y_arr_[i_ - 1]) / (2 * h_))
    return y_arr_derivative_


def der_2_ord2(y_arr_, n_, h_):
    y_arr_derivative_ = np.array([])
    for i_ in range(1, n_ - 1):
        y_arr_derivative_ = np.append(y_arr_derivative_,
                                      (y_arr_[i_ + 1] - 2 * y_arr_[i_] +
                                       y_arr_[i_ - 1]) / h_ ** 2)
    return y_arr_derivative_


def der_2_ord4(y_arr_, n_, h_):
    y_arr_derivative_ = np.array([])
    for i_ in range(2, n_ - 2):
        y_arr_derivative_ = np.append(y_arr_derivative_,
                                      (-y_arr_[i_ + 2] + 16 * y_arr_[i_ + 1] -
                                       30 * y_arr_[i_] + 16 * y_arr_[i_ - 1] -
                                       y_arr_[i_ - 2]) / (12 * h_ ** 2))
    return y_arr_derivative_


a = -1.5
b = 1.5
print('Вычисление производной по заданному количеству точек')
n = int(input())
h = (b - a) / n
x_arr = np.linspace(a, b, n)
y_arr = function(x_arr)
y_arr_analytic = der_1_analytic(x_arr)
y_arr_analytic_2nd = der_2_analytic(x_arr)

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
plt.plot(x_arr_to_plot, y_arr_analytic_to_plot)
plt.plot(x_arr_to_plot, y_arr_derivative)
fig.suptitle('Вторая производная, четвертый порядок точности \n СКО = ' +
             str(mse(y_arr_analytic_to_plot, y_arr_derivative, len(y_arr_derivative))))


print('Построение графика зависимости среднеквдратического отколнения от количества точек')
n_min = int(input())
n_max = int(input())
n_arr = np.linspace(n_min, n_max, n_max - n_min + 1)
der1right_arr = np.array([])
der1central_arr = np.array([])
der2ord2_arr = np.array([])
der2ord4_arr = np.array([])
for i in range(n_min, n_max + 1):
    x_arr = np.linspace(a, b, i)
    y_arr = function(x_arr)
    h = (b - a) / i

    der1analytic = der_1_analytic(x_arr)
    der1right = der_1_right(y_arr, i, h)
    der1right_arr = np.append(der1right_arr, mse(der1right, np.delete(der1analytic, i - 1), i))
    der1central = der_1_central(y_arr, i, h)
    der1central_arr = np.append(der1central_arr, mse(der1central, np.delete(der1analytic, [0, i - 1]), i))

    der2analytic = der_2_analytic(x_arr)
    der2ord2 = der_2_ord2(y_arr, i, h)
    der2ord2_arr = np.append(der2ord2_arr, mse(der2ord2, np.delete(der2analytic, [0, i - 1]), i))
    der2ord4 = der_2_ord4(y_arr, i, h)
    der2ord4_arr = np.append(der2ord4_arr, mse(der2ord4, np.delete(der2analytic, [0, 1, i - 1, i-2]), i))

fig = plt.figure()
plt.plot(n_arr, der1right_arr, label='Первая производная, правые разности')
plt.plot(n_arr, der1central_arr, label='Первая производная, центральные разности')
plt.legend()

fig = plt.figure()
plt.plot(n_arr, der2ord2_arr, label='Вторая производная, второй порядок')
plt.plot(n_arr, der2ord4_arr, label='Вторая производная, четвертый порядок')
plt.legend()
plt.show()
