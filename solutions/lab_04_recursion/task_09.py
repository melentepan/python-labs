# Задание 9. Напишите рекурсивное решение головоломки "Ханойская башня".


def hanoi(n, source='A', target='C', auxiliary='B'):
    if n < 0:
        raise ValueError('Количество дисков должно быть неотрицательным.')
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f'Диск {n}: {source} -> {target}')
    hanoi(n - 1, auxiliary, target, source)

def solve(n):
    if n < 0:
        print('Количество дисков должно быть неотрицательным.')
    else:
        hanoi(n)
        print('Количество ходов:', 2 ** n - 1)
