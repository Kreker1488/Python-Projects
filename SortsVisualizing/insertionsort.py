import random
import numpy as np
import matplotlib.pyplot as plt
import winsound
import sys

# Сортировка вставками

plt.ion()
fig, ax = plt.subplots()

def on_close(event):
    plt.close('all')
    sys.exit()
fig.canvas.mpl_connect('close_event', on_close)

if len(sys.argv) >= 3:
    n = int(sys.argv[1])
    pause_ms = int(sys.argv[2])
else:
    n = 10
    pause_ms = 100

x = np.arange(n)
y = np.arange(1, n+1)
random.shuffle(y)

colors = ['blue'] * n

ax.bar(x, y, color='blue')
ax.set_title("Сортировка вставками")
plt.show()
plt.pause(0.5)

for i in range(1, n):
    key = y[i]
    j = i - 1
    # подсветим текущий вставляемый элемент
    colors[i] = 'orange'
    ax.bar(x, y, color=colors)
    plt.draw()
    plt.pause(pause_ms/1000)

    while j >= 0 and y[j] > key:
        ax.clear()
        colors[j] = 'red'                           # сравниваемый
        colors[j+1] = 'orange'                      # текущий элемент (будет сдвигаться)
        winsound.Beep(500, pause_ms)

        y[j+1] = y[j]                               # сдвиг
        ax.bar(x, y, color=colors)
        ax.set_title(f"Сортировка вставками  вставлено {i}  сдвиг {j}")
        plt.draw()
        plt.pause(pause_ms/1000)

        colors[j] = 'blue'
        j -= 1

    y[j+1] = key
    # после вставки отмечаем отсортированную часть зелёным
    colors = ['green'] * (i+1) + ['blue'] * (n - i - 1)
    winsound.Beep(700, pause_ms)
    ax.clear()
    ax.bar(x, y, color=colors)
    ax.set_title(f"Сортировка вставками  вставлено {i}")
    plt.draw()
    plt.pause(0.05)

# Оповещение об окончании работы
colors = ['blue'] * n
for i in range(n):
    ax.clear()
    colors[i] = 'green'
    ax.bar(x, y, color=colors)
    plt.draw()
    winsound.Beep((i+1)*100, pause_ms)
    plt.pause(pause_ms/1000)

plt.pause(2)
plt.ioff()
plt.close('all')