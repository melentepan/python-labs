# Задание. Используя словесное и визуальное описание, реализовать сортировку выбором.

# Сортировка выбором ищет минимум в ещё не упорядоченной части списка.
# Меняем найденный минимум с первым элементом этой части.
# После этого расширяем упорядоченную часть на один элемент и повторяем поиск.
# Пример: [5, 1, 4, 2] -> [1, 5, 4, 2] -> [1, 2, 4, 5].
# На последнем проходе список [1, 2, 4, 5] остаётся без изменений.
# Список изменяется на месте. Время: O(N²) даже для готового списка.
# Дополнительная память: O(1). Взаимный порядок равных элементов может меняться.


def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        minimum_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[minimum_index]:
                minimum_index = j
        if minimum_index != i:
            numbers[i], numbers[minimum_index] = (numbers[minimum_index], numbers[i])
    return numbers

def solve(numbers):
    selection_sort(numbers)
    print('Отсортированный массив:', *numbers)


# numbers = list(map(float, input('Введите числа через пробел: ').split()))
# solve(numbers)
