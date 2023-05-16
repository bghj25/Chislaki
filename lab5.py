import numpy as np
import matplotlib.pyplot as plt


def etalon(x_):
    return np.tan(x_) + np.cos(np.tan(x_))


def f(x_, y1_, y2_):
    return 2 * np.tan(x_) * y2_ - np.power(np.cos(x_), -4) * y1_ + np.tan(x_) * np.power(np.cos(x_), -4)


# noinspection PyPep8Naming,PyShadowingNames
def euler(x_, y1_0_, y2_0_, h_, N_):
    y1_ = np.zeros(N_ + 1)
    y2_ = np.zeros(N_ + 1)
    y1_[0] = y1_0_
    y2_[0] = y2_0_

    for i in range(N_):
        y1_[i + 1] = y1_[i] + h_ * y2_[i]
        y2_[i + 1] = y2_[i] + h_ * f(x_[i], y1_[i], y2_[i])

    return y1_


def runge_kutta(x_, y1_0_, y2_0_, h_, N_):
    y1_ = np.zeros(N_ + 1)
    y2_ = np.zeros(N_ + 1)
    y1_[0] = y1_0_
    y2_[0] = y2_0_

    for i in range(N_):
        k1 = h_ * y2_[i]
        m1 = h_ * f(x_[i], y1_[i], y2_[i])
        k2 = h_ * (y2_[i] + 0.5 * m1)
        m2 = h_ * f(x_[i] + 0.5 * h_, y1_[i] + 0.5 * k1, y2_[i] + 0.5 * m1)
        k3 = h_ * (y2_[i] + 0.5 * m2)
        m3 = h_ * f(x_[i] + 0.5 * h_, y1_[i] + 0.5 * k2, y2_[i] + 0.5 * m2)
        k4 = h_ * (y2_[i] + m3)
        m4 = h_ * f(x_[i] + h_, y1_[i] + k3, y2_[i] + m3)
        y1_[i + 1] = y1_[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y2_[i + 1] = y2_[i] + (m1 + 2 * m2 + 2 * m3 + m4) / 6
    return y1_


def adams(x_, y1_0_, y2_0_, h_, N_):
    y1_ = np.zeros(N_ + 1)
    y2_ = np.zeros(N_ + 1)
    y1_[0] = y1_0_
    y2_[0] = y2_0_
    for i in range(2):
        k1 = h_ * y2_[i]
        m1 = h_ * f(x_[i], y1_[i], y2_[i])
        k2 = h_ * (y2_[i] + 0.5 * m1)
        m2 = h_ * f(x_[i] + 0.5 * h_, y1_[i] + 0.5 * k1, y2_[i] + 0.5 * m1)
        k3 = h_ * (y2_[i] + 0.5 * m2)
        m3 = h_ * f(x_[i] + 0.5 * h_, y1_[i] + 0.5 * k2, y2_[i] + 0.5 * m2)
        k4 = h_ * (y2_[i] + m3)
        m4 = h_ * f(x_[i] + h_, y1_[i] + k3, y2_[i] + m3)
        y1_[i + 1] = y1_[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y2_[i + 1] = y2_[i] + (m1 + 2 * m2 + 2 * m3 + m4) / 6

    for i in range(2, N_):
        m1 = h_ * f(x_[i], y1_[i], y2_[i])
        k1 = h_ * y2_[i]
        m2 = h_ * f(x_[i - 1], y1_[i - 1], y2_[i - 1])
        k2 = h_ * y2_[i - 1]
        m3 = h_ * f(x_[i - 2], y1_[i - 2], y2_[i - 2])
        k3 = h_ * y2_[i - 2]
        y1_[i + 1] = y1_[i] + (23 * k1 - 16 * k2 + 5 * k3) / 12
        y2_[i + 1] = y2_[i] + (23 * m1 - 16 * m2 + 5 * m3) / 12
    return y1_


x_0 = 0.0
y1_0 = 1.0
y2_0 = 1.0
N = 20
h = 1 / N
x = np.zeros(N + 1)
for i in range(N):
    x[i + 1] = x[i] + h

y_e = euler(x, y1_0, y2_0, h, N)
y_r = runge_kutta(x, y1_0, y2_0, h, N)
y_a = adams(x, y1_0, y2_0, h, N)
y_etalon = etalon(x)
plt.plot(x, y_etalon, label='эталонное решение', color='green')
plt.plot(x, y_e, label='метод Эйлера', color='red')
plt.plot(x, y_r, label='метод Рунге', color='blue')
plt.plot(x, y_a, label='метод Адамса', color='cyan')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()


N_min = 12  # h = 0.5
N_max = 300  # h = 0.001
h_max = 1 / N_min
h_min = 1 / N_max
number_of_points = N_max - N_min + 1

y_1_etalon = etalon(1)
ln_y1_e = np.zeros(number_of_points)
ln_y1_r = np.zeros(number_of_points)
ln_y1_a = np.zeros(number_of_points)
ln_h = np.zeros(number_of_points)

for i in range(N_min, N_max + 1):
    h = 1 / i
    ln_h[i - N_min] = h
    x = np.zeros(i + 1)
    for j in range(i):
        x[j + 1] = x[j] + h
    y_e = euler(x, y1_0, y2_0, h, i)
    y_r = runge_kutta(x, y1_0, y2_0, h, i)
    y_a = adams(x, y1_0, y2_0, h, i)
    ln_y1_e[i - N_min] = np.abs(y_e[len(y_e) - 1] - y_1_etalon)
    ln_y1_r[i - N_min] = np.abs(y_r[len(y_r) - 1] - y_1_etalon)
    ln_y1_a[i - N_min] = np.abs(y_a[len(y_a) - 1] - y_1_etalon)


fig = plt.figure()
plt.loglog(ln_h, ln_y1_e, label='метод Эйлера', color='red')
plt.loglog(ln_h, ln_y1_r, label='метод Рунге', color='blue')
plt.loglog(ln_h, ln_y1_a, label='метод Адамса', color='cyan')
plt.xlabel('log(h)')
plt.ylabel('log(|delta(y)|')
plt.legend()
plt.grid()
plt.show()

def get_slope(arr):
    return (arr[-1] - arr[0]) / (np.log(ln_h)[-1] - np.log(ln_h)[0])
print("euler", get_slope(np.log(ln_y1_e)))
print("runge", get_slope(np.log(ln_y1_r)))
print("adams", get_slope(np.log(ln_y1_a)))

N = 10
h = 1 / N
x = np.zeros(N + 1)
for j in range(N):
    x[j + 1] = x[j] + h
y_e1 = euler(x, y1_0, y2_0, h, N)
y_r1 = runge_kutta(x, y1_0, y2_0, h, N)
y_a1 = adams(x, y1_0, y2_0, h, N)

N = 20
h = 1 / N
x = np.zeros(N + 1)
for j in range(N):
    x[j + 1] = x[j] + h
print(x)
y_e2 = euler(x, y1_0, y2_0, h, N)
y_r2 = runge_kutta(x, y1_0, y2_0, h, N)
y_a2 = adams(x, y1_0, y2_0, h, N)

print('Эйлер', np.abs(y_e1[len(y_e1) - 1] - y_e2[len(y_e2) - 1]) / 1, 'sss', np.abs(y_e2[len(y_e2) - 1] - y_1_etalon))
print('Рунге', np.abs(y_r1[len(y_r1) - 1] - y_r2[len(y_r2) - 1]) / 15, 'sss', np.abs(y_r2[len(y_r2) - 1] - y_1_etalon))
print('Адамс', np.abs(y_a1[len(y_a1) - 1] - y_a2[len(y_a2) - 1]) / 7, 'sss', np.abs(y_a2[len(y_a2) - 1] - y_1_etalon))
