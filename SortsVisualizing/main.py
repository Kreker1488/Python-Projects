import subprocess
import tkinter as tk
from tkinter import ttk
import sys

process = None
def run_sort(choise):
    n = int(size_var.get())
    pause = int(pause_var.get())
    script_map = {
        1: 'bubblesort.py',
        2: 'insertionsort.py',
        3: 'selectionsort.py',
        4: 'quicksort.py',
        5: 'shakersort.py',
        6: 'gnomesort.py'
    }
    script = script_map.get(choise)
    process = subprocess.Popen([sys.executable, script, str(n), str(pause)])

def exit():
    global process
    if process and process.poll() is None:
        process.terminate()
        process.wait()
    root.destroy()

root = tk.Tk()
root.title('Сортировка')
root.geometry('600x600')
root.configure(bg='#E6E6FA')

lbl_font = ('Arial', 14)

tk.Label(root, text='Количество элементов:', font=lbl_font, bg='#E6E6FA').pack(pady=5)
size_var = tk.StringVar(value='30')
ttk.Spinbox(root, from_=10, to=100, textvariable=size_var, width=10).pack()

tk.Label(root, text='Задержка итераций в мс:', font=lbl_font, bg='#E6E6FA').pack(pady=5)
pause_var = tk.StringVar(value='30')
ttk.Spinbox(root, from_=10, to=100, textvariable=pause_var, width=10).pack()

tk.Label(root, text='Выберите сортировку:', font=lbl_font, bg='#E6E6FA').pack(pady=10)
btn_frame_1 = tk.Frame(root, bg='#E6E6FA')
btn_frame_1.pack(pady=5)
btn_frame_2 = tk.Frame(root, bg='#E6E6FA')
btn_frame_2.pack(pady=5)

btn_width = 10
btn_height = 2
btn_font=('Arial', 12, 'bold')
btn_bg='#E6E6FA'
tk.Button(btn_frame_1, text='Пузырек', font=btn_font, width=btn_width, height=btn_height, bg=btn_bg, command=lambda: run_sort(1)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_1, text='Вставками', font=btn_font, width=btn_width, height=btn_height, bg=btn_bg, command=lambda: run_sort(2)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_1, text='Выбором', font=btn_font, width=btn_width, height=btn_height, bg=btn_bg, command=lambda: run_sort(3)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_2, text='Быстрая', font=btn_font, width=btn_width, height=btn_height, bg=btn_bg, command=lambda: run_sort(4)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_2, text='Шейкерная', font=btn_font, width=btn_width, height=btn_height, bg=btn_bg, command=lambda: run_sort(5)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_2, text='Гномья', font=btn_font, width=btn_width, height=btn_height, bg=btn_bg, command=lambda: run_sort(6)).pack(side=tk.LEFT, padx=5)

tk.Button(root, text="Выход", font=btn_font, width=btn_width, height=btn_height, command=exit, bg="lightcoral").pack(side=tk.BOTTOM, pady=15)







root.mainloop()