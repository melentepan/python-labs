# Задание 5. Дано целое число. Вывести его строку-описание вида «отрицательное четное число»,
# «нулевое число», «положительное нечетное число» и т. д.


def solve(number):
    if number == 0:
        print('нулевое число')
    else:
        if number < 0:
            sign = 'отрицательное'
        else:
            sign = 'положительное'
        if number % 2 == 0:
            parity = 'четное'
        else:
            parity = 'нечетное'
        print(sign, parity, 'число')


# number = int(input("Введите number: "))
# solve(number)
