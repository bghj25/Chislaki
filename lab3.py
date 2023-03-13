import numpy as np
import matplotlib.pyplot as plt
import math


def function(x_arr_):
    return 1 / (1 + np.cos(x_arr_ / 5))


def rect(y_arr_, a_, b_, n_):
    return (b_ - a_) * np.sum(y_arr_) / n_


def trap(y_arr_, a_, b_, n_):
    return (b_ - a_) * ((y_arr_[0] + y_arr_[n_ - 1]) / 2 +
                        np.sum(y_arr_, initial=-y_arr_[0] - y_arr_[n_ - 1])) / n_


def simpson(y_arr_, a_, b_, n_):
    integral_ = 0
    for i_ in range(0, math.ceil(n_ / 2) - 1):
        integral_ += (b - a) / (3 * n_) * (y_arr_[2 * i_] + y_arr_[2 * i_ + 2] + 4 * y_arr_[2 * i_ + 1])
    if n_ % 2 == 0:  # учитываем кусочек на который не хватило параболы, если такой есть
        integral_ += y_arr_[n_ - 1] * (b - a) / n_
    return integral_


a = -3
b = 3

n_min = int(input())
n_max = int(input())
integral = 10 * np.tan(3 / 10)
integral_rect = np.array([])
integral_trap = np.array([])
integral_simpson = np.array([])
for i in range(n_min, n_max + 1):
    x_arr = np.linspace(a, b, i)
    y_arr = function(x_arr)
    integral_rect = np.append(integral_rect, rect(y_arr, a, b, i))
    integral_trap = np.append(integral_trap, trap(y_arr, a, b, i))
    integral_simpson = np.append(integral_simpson, simpson(y_arr, a, b, i))
n_arr = np.linspace(n_min, n_max, n_max - n_min + 1)
plt.plot(n_arr, abs(integral_rect - integral), label='Прямоугольники')
plt.plot(n_arr, abs(integral_trap - integral), label='Трапеции')
plt.plot(n_arr, abs(integral_simpson - integral), label='Симпсон')
plt.legend()
plt.show()
