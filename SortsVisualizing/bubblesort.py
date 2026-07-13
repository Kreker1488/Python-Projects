import random
import sys
import numpy as np
import matplotlib.pyplot as plt
import winsound

# Пузырьковая сортировка

# Создаем холст и поле для графика
plt.ion()
fig = plt.figure()
ax = fig.add_subplot()

def on_close(event):
    plt.close('all')
    sys.exit()
fig.canvas.mpl_connect('close_event', on_close)

# Передаем аргументы из main файла
if len(sys.argv) >= 3:
    n = int(sys.argv[1])
    pause_ms = int(sys.argv[2])
else:
    n = 10
    pause_ms = 100

# Создаем координатные оси и перемешиваем столбцы
x = np.arange(n)
y = np.arange(1, n+1)
random.shuffle(y)

# Функция для пузырьковой сортировки
colors = ['blue'] * n                                   # Окрашиваем все столбцы в синий
for i in range(n):
    for j in range(n - i - 1):
        ax.clear()                                      # Каждую итерацию очищаем холст
        colors[j] = 'green'                             # Окрашиваем текущий столбец, чтобы было наглядней
        if y[j] > y[j+1]:
            colors[j+1] = 'red'
            winsound.Beep(1000, pause_ms)  # Просто звуковое сопровождение
            y[j], y[j+1] = y[j+1], y[j]
        ax.bar(x, y, color=colors)                      # Задаем параметры графика
        ax.set_title(f"Пузырьковая сортировка")
        plt.draw()                                      # Выводим график на экран
        winsound.Beep(500, pause_ms)
        plt.pause(pause_ms/1000)                                  # Небольшая пауза
        colors[j] = 'blue'
        colors[j + 1] = 'blue'

# Оповещение об окончании работы
for i in range(n):
    ax.clear()
    colors[i] = 'green'
    ax.bar(x, y, color=colors)
    plt.draw()
    winsound.Beep((i+1)*100, pause_ms)
    plt.pause(pause_ms/1000)

plt.pause(0.5)
plt.ioff()
plt.close('all')