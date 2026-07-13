import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import winsound

# Быстрая сортировка

# Чтение аргументов
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

# Обработчик закрытия окна
def on_close(event):
    plt.close('all')
    sys.exit()
fig.canvas.mpl_connect('close_event', on_close)

stack = [(0, len(y) - 1)]
while stack:
    lo, hi = stack.pop()
    if lo >= hi:
        continue
    # Разбиение
    pivot = y[hi]
    i = lo
    for j in range(lo, hi):
        # Визуализация сравнения
        colors = ['blue'] * len(y)
        colors[j] = 'red'
        colors[hi] = 'orange'   # опорный элемент
        colors[i] = 'yellow'    # текущий индекс для обмена
        ax.clear()
        ax.bar(x, y, color=colors)
        ax.set_title(f'Быстрая сортировка')
        plt.draw()
        plt.pause(pause_ms)
        winsound.Beep(400, int(pause_ms*1000))

        if y[j] <= pivot:
            y[i], y[j] = y[j], y[i]
            i += 1
            winsound.Beep(600, int(pause_ms*1000))
    # Ставим pivot на место
    y[i], y[hi] = y[hi], y[i]
    # Визуализация обмена с опорным
    colors = ['blue'] * len(y)
    colors[i] = 'green'   # опорный встал на место
    ax.clear()
    ax.bar(x, y, color=colors)
    ax.set_title(f'Быстрая сортировка  pivot помещен в {i}')
    plt.draw()
    plt.pause(pause_ms)
    winsound.Beep(900, int(pause_ms*1000))

    # Добавляем подмассивы в стек (сначала правый, потом левый)
    stack.append((i + 1, hi))
    stack.append((lo, i - 1))

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