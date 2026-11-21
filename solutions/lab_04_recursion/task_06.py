# Задание 6. Обратный порядок слов: Напишите функцию, которая рекурсивно меняет порядок слов в
# заданной строке на обратный.


def reverse_words(text):
    words = text.split()
    result = []

    def collect(index):
        if index < 0:
            return
        result.append(words[index])
        collect(index - 1)
    collect(len(words) - 1)
    return ' '.join(result)

def solve(text):
    print('Обратный порядок слов:', reverse_words(text))
