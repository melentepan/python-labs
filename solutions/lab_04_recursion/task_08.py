# Задание 8. Подсчет количества цифр в числе: Напишите функцию, которая рекурсивно подсчитывает
# количество цифр в заданном числе.


def count_digits(number):
    number = abs(number)
    if number < 10:
        return 1
    return 1 + count_digits(number // 10)

def solve(number):
    print('Количество цифр:', count_digits(number))


# number = int(input("Введите number: "))
# solve(number)
