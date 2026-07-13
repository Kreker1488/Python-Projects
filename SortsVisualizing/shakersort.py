import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import winsound

# Шейкерная сортировка

if len(sys.argv) >= 3:
    n = int(sys.argv[1])
    pause_ms = int(sys.argv[2]) / 1000
else:
    n = 30
    pause_ms = 0.05

plt.ion()
fig, ax = plt.subplots()
x = np.arange(n)
y = np.arange(1, n + 1)
random.shuffle(y)

def on_close(event):
    plt.close('all')
    sys.exit()
fig.canvas.mpl_connect('close_event', on_close)

left = 0
right = len(y) - 1
swapped = True
while swapped:
    swapped = False
    # Проход слева направо
    for i in range(left, right):
        colors = ['blue'] * len(y)
        colors[i] = 'red'
        colors[i+1] = 'red'
        ax.clear()
        ax.bar(x, y, color=colors)
        ax.set_title(f'Шейкерная сортировка  слева={left} справа={right}  →')
        plt.draw()
        plt.pause(pause_ms)
        winsound.Beep(350, int(pause_ms*1000))
        if y[i] > y[i+1]:
            y[i], y[i+1] = y[i+1], y[i]
            swapped = True
            winsound.Beep(700, int(pause_ms*1000))
    if not swapped:
        break
    right -= 1
    # Проход справа налево
    for i in range(right - 1, left - 1, -1):
        colors = ['blue'] * len(y)
        colors[i] = 'red'
        colors[i+1] = 'red'
        ax.clear()
        ax.bar(x, y, color=colors)
        ax.set_title(f'Шейкерная сортировка  слева={left} справа={right}  ←')
        plt.draw()
        plt.pause(pause_ms)
        winsound.Beep(350, int(pause_ms*1000))
        if y[i] > y[i+1]:
            y[i], y[i+1] = y[i+1], y[i]
            swapped = True
            winsound.Beep(700, int(pause_ms*1000))
    left += 1
    # Подсветка отсортированных границ
    colors = ['blue'] * len(y)
    for k in range(left):
        colors[k] = 'green'
    for k in range(right + 1, len(y)):
        colors[k] = 'green'
    ax.clear()
    ax.bar(x, y, color=colors)
    ax.set_title(f'Шейкерная сортировка  границы закреплены')
    plt.draw()
    plt.pause(pause_ms)

# Оповещение об окончании работы
colors = ['blue'] * n
for i in range(n):
    ax.clear()
    colors[i] = 'green'
    ax.bar(x, y, color=colors)
    plt.draw()
    winsound.Beep((i+1)*100, int(pause_ms*1000))
    plt.pause(pause_ms)

plt.ioff()
plt.close('all')