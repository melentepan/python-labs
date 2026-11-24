# Задание. Используя словесное описание, реализовать обход дерева.

# Каждый узел — объект Node со значением и двумя ссылками на потомков.
# None означает, что узла нет.
# При построении дерева меньшие значения идут влево, остальные вправо.
# Симметричный обход: левое поддерево, текущий узел, правое поддерево.
# В дереве поиска такой обход выводит числа по возрастанию.
# Поиск идёт влево или вправо в зависимости от искомого значения.
# При выводе структуры отступы показывают глубину узла.


class Node:
    def __init__(self, value):
        # При создании узла сохраняем число; потомков пока нет.
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        # Дошли до пустой ветки — создаём здесь новый узел.
        return Node(value)
    if value < root.value:
        # Меньшее число добавляем в левую ветку и сохраняем ссылку на неё.
        root.left = insert(root.left, value)
    else:
        # Большее или равное число добавляем в правую ветку.
        root.right = insert(root.right, value)
    # Возвращаем текущий узел вместе с добавленной веткой.
    return root

def search(root, value):
    # Пустая ветка означает отсутствие числа, равенство — успешный поиск.
    # Если root равен None, часть после or уже не проверяется.
    if root is None or root.value == value:
        return root
    if value < root.value:
        # Меньшее число может находиться только слева.
        return search(root.left, value)
    # Если число больше текущего, продолжаем поиск справа.
    return search(root.right, value)


def inorder_traversal(root):
    if root is None:
        # Пустую ветку обходить не нужно — останавливаем этот вызов.
        return
    # Сначала полностью обходим левую ветку с меньшими числами.
    inorder_traversal(root.left)
    # Затем печатаем текущий узел и обходим правую ветку.
    print(root.value, end=' ')
    inorder_traversal(root.right)


def show_tree(root, level=0, label='Корень'):
    if root is None:
        return
    # Каждый уровень добавляет четыре пробела перед подписью узла.
    print('    ' * level + f'{label}: {root.value}')
    # Потомки находятся на уровень глубже текущего узла.
    show_tree(root.left, level + 1, 'Слева')
    show_tree(root.right, level + 1, 'Справа')


def solve(values, target):
    # Начинаем с пустого дерева и по очереди добавляем входные числа.
    root = None
    for value in values:
        # Присваивание сохраняет корень, в том числе после первой вставки.
        root = insert(root, value)
    print('Структура дерева:')
    show_tree(root)
    if root is None:
        print('Дерево пустое.')
    # Поиск возвращает найденный узел или None, если числа нет.
    result = search(root, target)
    if result is None:
        print('Элемент не найден:', target)
    else:
        print('Элемент найден:', result.value)
    # В дереве поиска симметричный обход выводит числа по неубыванию.
    print('Симметричный обход дерева:', end=' ')
    inorder_traversal(root)
    print()


# values = list(map(float, input('Введите числа через пробел: ').split()))
# target = float(input('Введите искомое число: '))
# solve(values, target)
