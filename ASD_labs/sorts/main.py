arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

'''
Сортировка методом прочесывания

Характеристика	Значение
Лучший случай	O(n log n)
Средний случай	O(n² / 2^p), где p — число шагов; на практике ≈ O(n log n)
Худший случай	O(n²)
Память	        O(1) — сортировка на месте
Устойчивость	Нет (неустойчивая)
'''
def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(n - gap):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swapped = True
    return arr

'''
Сортировка вставками

Характеристика	Значение
Лучший случай	O(n) — массив уже отсортирован (одно сравнение на элемент)
Средний случай	O(n²)
Худший случай	O(n²) — массив отсортирован по убыванию
Память	        O(1) — на месте
Устойчивость	Да, устойчивая
'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

'''
Сортировка выбором

Характеристика	Значение
Лучший случай	O(n²)
Средний случай	O(n²)
Худший случай	O(n²)
Число сравнений	Всегда n(n-1)/2 — не зависит от данных!
Число перестановок	от 0 (уже отсортирован) до n-1
Память	O(1) — на месте
Устойчивость	Нет ❌
'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr