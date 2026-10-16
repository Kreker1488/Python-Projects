# 1 ЛАБА
"""
_s = input('Введите строку')
s = []
for i in _s:
    if i in '(){}[]':
        s.append(i)

d = {'(': ')', '[': ']', '{': '}'}
while s:
    flag = False
    for j in range(len(s) - 1):
        if s[j] in '({[':
            if d[s[j]] == s[j+1]:
                s.pop(j+1)
                s.pop(j)
                flag = True
                break
    if not flag:
        break
if not s:
    print("Строка существует")
else:
    print("Строка не существует")
"""

# 2 ЛАБА
"""
s = input("Введите выражение: ").replace(" ", "")

# выражение заканчивается на '='
if not s.endswith('='):
    print("Ошибка: выражение должно заканчиваться на '='")
    exit()

expr = s[:-1]

# пустое выражение
if expr == "":
    print("Ошибка: пустое выражение")
    exit()

# допустимые символы
allowed = set("0123456789.+-*/()")
if not set(expr) <= allowed:
    bad = set(expr) - allowed
    print(f"Ошибка: недопустимые символы {bad}")
    exit()

# скобки
stack = []
pairs = {')': '(', ']': '[', '}': '{'}
for c in expr:
    if c in "([{":
        stack.append(c)
    elif c in ")]}":
        if not stack or stack[-1] != pairs[c]:
            print("Ошибка: скобки расставлены неверно")
            exit()
        stack.pop()
if stack:
    print("Ошибка: скобки расставлены неверно")
    exit()

# деление на ноль
try:
    result = eval(expr)
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
    exit()
except SyntaxError:
    print("Ошибка: некорректное выражение")
    exit()

print(f"Результат: {result}")
"""

# 3 ЛАБА
"""
try:
    x = int(input("Введите число x: "))
except ValueError:
    print("Ошибка: нужно ввести целое число")
    exit()

if x < 1:
    print("Ошибка: x должно быть >= 1")
    exit()

result = []

p3 = 1
while p3 <= x:
    p5 = 1
    while p3 * p5 <= x:
        p7 = 1
        while p3 * p5 * p7 <= x:
            result.append(p3 * p5 * p7)
            p7 *= 7
        p5 *= 5
    p3 *= 3

result.sort()

print(f"Числа от 1 до {x} вида 3^K * 5^L * 7^M:")
print(*result)
"""
