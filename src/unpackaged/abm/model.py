import random

x0 = 0
y0 = 0
x1 = 50
y1 = 50
rnd_number_0 = random.random()
rnd_number_1 = random.random()

if rnd_number_0 < 0.5:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1

if rnd_number_1 < 0.5:
    y1 += 1
    x1 += 1
else:
    y1 -= 1
    x1 -= 1


y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)
