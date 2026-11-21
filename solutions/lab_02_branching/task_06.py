# Задание 6. Дано целое число, лежащее в диапазоне 1–999. Вывести его строку описание вида «четное
# двузначное число», «нечетное трехзначное число» и т. д.


def solve(number):
    if number < 1 or number > 999:
        print('Число должно быть в диапазоне от 1 до 999.')
    else:
        if number % 2 == 0:
            parity = 'четное'
        else:
            parity = 'нечетное'
        if number < 10:
            digits = 'однозначное'
        elif number < 100:
            digits = 'двузначное'
        else:
            digits = 'трехзначное'
        print(parity, digits, 'число')
