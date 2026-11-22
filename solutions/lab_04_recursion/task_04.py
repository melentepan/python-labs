# Задание 4. Палиндром: Напишите функцию, которая рекурсивно проверяет, является ли заданная
# строка палиндромом.


def is_palindrome(text):

    def check(left, right):
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return check(left + 1, right - 1)
    return check(0, len(text) - 1)

def solve(text):
    if is_palindrome(text):
        print('Строка является палиндромом.')
    else:
        print('Строка не является палиндромом.')


# text = input("Введите строку: ")
# solve(text)
