from solutions.lab_04_recursion.task_01 import solve as task_01
from solutions.lab_04_recursion.task_02 import solve as task_02
from solutions.lab_04_recursion.task_03 import solve as task_03
from solutions.lab_04_recursion.task_04 import solve as task_04
from solutions.lab_04_recursion.task_05 import solve as task_05
from solutions.lab_04_recursion.task_06 import solve as task_06
from solutions.lab_04_recursion.task_07 import solve as task_07
from solutions.lab_04_recursion.task_08 import solve as task_08
from solutions.lab_04_recursion.task_09 import solve as task_09


print('\n\n' + '#' * 80)
print('ЛАБОРАТОРНАЯ РАБОТА 4 — РЕКУРСИЯ')
print('#' * 80)

print('\n' + '=' * 70)
print('ЗАДАЧА 1. Факториал')
print('Условие: Задание 1. Факториал числа: Напишите функцию, которая рекурсивно вычисляет факториал заданного числа n.')
n = 5
print('Входные данные:')
print('n =', n)
print('Результат:')
task_01(n)

print('\n' + '=' * 70)
print('ЗАДАЧА 2. Числа Фибоначчи')
print('Условие: Задание 2. Числа Фибоначчи: Напишите функцию, которая рекурсивно вычисляет n-ое число Фибоначчи.')
n = 10
print('Входные данные:')
print('n =', n)
print('Результат:')
task_02(n)

print('\n' + '=' * 70)
print('ЗАДАЧА 3. Возведение в степень')
print('Условие: Задание 3. Возведение в степень: Напишите функцию, которая рекурсивно возводит число x в степень n.')
x = 2.0
n = 3
print('Входные данные:')
print('x =', x)
print('n =', n)
print('Результат:')
task_03(x, n)

print('\n' + '=' * 70)
print('ЗАДАЧА 4. Палиндром')
print('Условие: Задание 4. Палиндром: Напишите функцию, которая рекурсивно проверяет, является ли заданная строка палиндромом.')
text = 'топот'
print('Входные данные:')
print('text =', text)
print('Результат:')
task_04(text)

print('\n' + '=' * 70)
print('ЗАДАЧА 5. Рекурсивный бинарный поиск')
print('Условие: Задание 5. Бинарный поиск: Напишите функцию, которая рекурсивно выполняет бинарный поиск заданного элемента в отсортированном массиве.')
numbers = [1.0, 3.0, 5.0, 7.0, 9.0]
target = 7.0
print('Входные данные:')
print('Массив:', numbers)
print('target =', target)
print('Результат:')
task_05(numbers, target)

print('\n' + '=' * 70)
print('ЗАДАЧА 6. Обратный порядок слов')
print('Условие: Задание 6. Обратный порядок слов: Напишите функцию, которая рекурсивно меняет порядок слов в заданной строке на обратный.')
text = 'один два три'
print('Входные данные:')
print('text =', text)
print('Результат:')
task_06(text)

print('\n' + '=' * 70)
print('ЗАДАЧА 7. Сумма простых чисел')
print('Условие: Задание 7. Разложение числа на сумму простых чисел: Напишите функцию, которая рекурсивно разлагает заданное число на сумму простых чисел.')
n = 7
print('Входные данные:')
print('n =', n)
print('Результат:')
task_07(n)

print('\n' + '=' * 70)
print('ЗАДАЧА 8. Количество цифр')
print('Условие: Задание 8. Подсчет количества цифр в числе: Напишите функцию, которая рекурсивно подсчитывает количество цифр в заданном числе.')
number = -1200
print('Входные данные:')
print('number =', number)
print('Результат:')
task_08(number)

print('\n' + '=' * 70)
print('ЗАДАЧА 9. Ханойская башня')
print('Условие: Задание 9. Напишите рекурсивное решение головоломки "Ханойская башня".')
n = 3
print('Входные данные:')
print('n =', n)
print('Результат:')
task_09(n)
