import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import winsound

# Гномья сортировка

if len(sys.argv) >= 3:
    n = int(sys.argv[1])
    pause_ms = int(sys.argv[2]) / 1000.0
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


i = 0
while i < len(y):
    if i == 0 or y[i-1] <= y[i]:
        # подсветка текущего элемента
        colors = ['blue'] * len(y)
        colors[i] = 'green'
        ax.clear()
        ax.bar(x, y, color=colors)
        ax.set_title(f'Гномья сортировка  i={i}')
        plt.draw()
        plt.pause(pause_ms)
        i += 1
    else:
        # меняем местами
        y[i-1], y[i] = y[i], y[i-1]
        winsound.Beep(600, int(pause_ms*1000))
        # подсветка обмениваемых
        colors = ['blue'] * len(y)
        colors[i-1] = 'red'
        colors[i] = 'red'
        ax.clear()
        ax.bar(x, y, color=colors)
        ax.set_title(f'Гномья сортировка  поменялись {i-1} и {i}')
        plt.draw()
        plt.pause(pause_ms)
        i -= 1

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