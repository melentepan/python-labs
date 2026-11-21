from solutions.lab_01_linear_algorithms.task_01 import solve as task_01
from solutions.lab_01_linear_algorithms.task_02 import solve as task_02
from solutions.lab_01_linear_algorithms.task_03 import solve as task_03
from solutions.lab_01_linear_algorithms.task_04 import solve as task_04
from solutions.lab_01_linear_algorithms.task_05 import solve as task_05
from solutions.lab_01_linear_algorithms.task_06 import solve as task_06
from solutions.lab_01_linear_algorithms.task_07 import solve as task_07
from solutions.lab_01_linear_algorithms.task_08 import solve as task_08
from solutions.lab_01_linear_algorithms.task_09 import solve as task_09
from solutions.lab_01_linear_algorithms.task_10 import solve as task_10
from solutions.lab_01_linear_algorithms.task_11 import solve as task_11
from solutions.lab_01_linear_algorithms.task_12 import solve as task_12


print('\n\n' + '#' * 80)
print('ЛАБОРАТОРНАЯ РАБОТА 1 — ЛИНЕЙНЫЕ АЛГОРИТМЫ')
print('#' * 80)

print('\n' + '=' * 70)
print('ЗАДАЧА 1. Площадь и периметр прямоугольника')
print('Условие: Задание 1. Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b).')
a = 3.0
b = 4.0
print('Входные данные:')
print('a =', a)
print('b =', b)
print('Результат:')
task_01(a, b)

print('\n' + '=' * 70)
print('ЗАДАЧА 2. Длина окружности')
print('Условие: Задание 2. Дан диаметр окружности d. Найти ее длину L = π·d. В качестве значения π использовать 3.14.')
diameter = 10.0
print('Входные данные:')
print('diameter =', diameter)
print('Результат:')
task_02(diameter)

print('\n' + '=' * 70)
print('ЗАДАЧА 3. Среднее арифметическое')
print('Условие: Задание 3. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2.')
a = 4.0
b = 10.0
print('Входные данные:')
print('a =', a)
print('b =', b)
print('Результат:')
task_03(a, b)

print('\n' + '=' * 70)
print('ЗАДАЧА 4. Действия с квадратами')
print('Условие: Задание 4. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.')
a = -3.0
b = 2.0
print('Входные данные:')
print('a =', a)
print('b =', b)
print('Результат:')
task_04(a, b)

print('\n' + '=' * 70)
print('ЗАДАЧА 5. Действия с модулями')
print('Условие: Задание 5. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.')
a = -3.0
b = -2.0
print('Входные данные:')
print('a =', a)
print('b =', b)
print('Результат:')
task_05(a, b)

print('\n' + '=' * 70)
print('ЗАДАЧА 6. Расстояние между точками')
print('Условие: Задание 6. Найти расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2)')
x1 = 0.0
y1 = 0.0
x2 = 3.0
y2 = 4.0
print('Входные данные:')
print('x1 =', x1)
print('y1 =', y1)
print('x2 =', x2)
print('y2 =', y2)
print('Результат:')
task_06(x1, y1, x2, y2)

print('\n' + '=' * 70)
print('ЗАДАЧА 7. Длины AC и BC')
print('Условие: Задание 7. Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.')
a = -2.0
b = 5.0
c = 1.0
print('Входные данные:')
print('a =', a)
print('b =', b)
print('c =', c)
print('Результат:')
task_07(a, b, c)

print('\n' + '=' * 70)
print('ЗАДАЧА 8. Произведение длин AC и BC')
print('Условие: Задание 8. Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC')
a = 0.0
b = 10.0
c = 3.0
print('Входные данные:')
print('a =', a)
print('b =', b)
print('c =', c)
print('Результат:')
task_08(a, b, c)

print('\n' + '=' * 70)
print('ЗАДАЧА 9. Прямоугольник по вершинам')
print('Условие: Задание 9. Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2, y2). Стороны прямоугольника параллельны осям координат. Найти периметр и площадь данного прямоугольника.')
x1 = 1.0
y1 = 2.0
x2 = 5.0
y2 = 5.0
print('Входные данные:')
print('x1 =', x1)
print('y1 =', y1)
print('x2 =', x2)
print('y2 =', y2)
print('Результат:')
task_09(x1, y1, x2, y2)

print('\n' + '=' * 70)
print('ЗАДАЧА 10. Периметр и площадь треугольника')
print('Условие: Задание 10. Даны координаты трех вершин треугольника: (x1, y1), (x2, y2), (x3, y3). Найти его периметр и площадь')
x1 = 0.0
y1 = 0.0
x2 = 3.0
y2 = 0.0
x3 = 0.0
y3 = 4.0
print('Входные данные:')
print('x1 =', x1)
print('y1 =', y1)
print('x2 =', x2)
print('y2 =', y2)
print('x3 =', x3)
print('y3 =', y3)
print('Результат:')
task_10(x1, y1, x2, y2, x3, y3)

print('\n' + '=' * 70)
print('ЗАДАЧА 11. Значение функции 3x^6 - 6x^2 - 7')
print('Условие: Задание 11. Найти значение функции y = 3x^6 − 6x^2 − 7 при данном значении x')
x = 2.0
print('Входные данные:')
print('x =', x)
print('Результат:')
task_11(x)

print('\n' + '=' * 70)
print('ЗАДАЧА 12. Значение функции со степенями x - 3')
print('Условие: Задание 12. Найти значение функции y = 4(x−3)^6 − 7(x−3)^3 + 2 при данном значении x')
x = 2.0
print('Входные данные:')
print('x =', x)
print('Результат:')
task_12(x)
