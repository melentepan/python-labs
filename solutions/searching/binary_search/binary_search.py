# Задание. Используя словесное описание, реализовать бинарный поиск.

# Бинарный поиск работает со списком, заранее упорядоченным по возрастанию.
# Сравниваем искомое число со средним элементом текущего участка.
# Если искомое больше, продолжаем справа; если меньше — слева.
# При равенстве запоминаем индекс и продолжаем слева, чтобы найти первое вхождение.
# Если границы пересеклись, поиск завершён. Функция возвращает индекс от 0
# или -1 при отсутствии числа. При выводе индекс преобразуется в номер от 1.
# Пример: в [1, 3, 3, 7, 9] поиск 3 вернёт индекс 1, то есть номер 2.
# Время поиска: O(log N), дополнительная память: O(1).
# Консольная программа отдельно проверяет порядок элементов за O(N).


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] < target:
            left = middle + 1
        else:
            if numbers[middle] == target:
                result = middle
            right = middle - 1
    return result

def solve(numbers, target):
    n = len(numbers)
    ordered = True
    for i in range(1, n):
        if numbers[i] < numbers[i - 1]:
            ordered = False
            break
    if not ordered:
        print('Для бинарного поиска элементы должны идти по возрастанию.')
    else:
        index = binary_search(numbers, target)
        if index == -1:
            print('Число не найдено.')
        else:
            print('Номер первого вхождения:', index + 1)
