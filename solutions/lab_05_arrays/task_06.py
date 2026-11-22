# Задание 6. Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N). Найти среднее
# арифметическое элементов массива с номерами от K до L включительно.


def solve(numbers, k, l):
    total = 0.0
    for i in range(k - 1, l):
        total += numbers[i]
    average = total / (l - k + 1)
    print('Среднее арифметическое:', average)


# numbers = list(map(float, input('Введите числа через пробел: ').split()))
# k = int(input("Введите k: "))
# l = int(input("Введите l: "))
# solve(numbers, k, l)
