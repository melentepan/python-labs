# Задание. Используя словесное описание, реализовать обход дерева.

# Каждый узел — словарь со значением и двумя ссылками на потомков.
# None означает, что узла нет.
# При построении дерева меньшие значения идут влево, остальные вправо.
# Прямой обход: выводим корень, обходим левое поддерево, затем правое.
# Например, для ввода 4, 2, 6, 1, 3 получим обход 4, 2, 1, 3, 6.


def insert(root, value):
    if root is None:
        return {'value': value, 'left': None, 'right': None}
    if value < root['value']:
        root['left'] = insert(root['left'], value)
    else:
        root['right'] = insert(root['right'], value)
    return root

def preorder(root):
    if root is None:
        return
    print(root['value'], end=' ')
    preorder(root['left'])
    preorder(root['right'])

def solve(values):
    root = None
    for value in values:
        root = insert(root, value)
    print('Прямой обход дерева:', end=' ')
    preorder(root)
    print()


# values = list(map(float, input('Введите числа через пробел: ').split()))
# solve(values)
