import random
import numpy as np
import matplotlib.pyplot as plt
import winsound
import sys

# Сортировка выбором

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
ax.set_title("Selection Sort")
plt.show()
plt.pause(0.5)

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        ax.clear()
        colors[i] = 'yellow'   # текущий кандидат на минимум
        colors[j] = 'red'      # сравниваемый
        winsound.Beep(350, pause_ms)

        ax.bar(x, y, color=colors)
        ax.set_title(f"Selection Sort  find min  i={i}  j={j}")
        plt.draw()
        plt.pause(pause_ms/1000)

        if y[j] < y[min_idx]:
            min_idx = j
        colors[i] = 'blue'
        colors[j] = 'blue'

    # обмен, если нашли новый минимум
    if min_idx != i:
        y[i], y[min_idx] = y[min_idx], y[i]
        winsound.Beep(900, pause_ms)

    # помечаем i-й элемент как отсортированный
    colors = ['green'] * (i+1) + ['blue'] * (n - i - 1)
    ax.clear()
    ax.bar(x, y, color=colors)
    ax.set_title(f"Сортировка выбором")
    plt.draw()
    plt.pause(pause_ms/1000)

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