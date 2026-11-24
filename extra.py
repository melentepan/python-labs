from solutions.lab_07_bubble_sort.bubble_sort import solve as task_01
from solutions.lab_08_insertion_sort.insertion_sort import solve as task_02
from solutions.lab_09_selection_sort.selection_sort import solve as task_03
from solutions.lab_10_binary_search.binary_search import solve as task_04
from solutions.lab_11_tree_traversal.tree_traversal import solve as task_05
from solutions.lab_12_queue.queue import Queue


print('\n\n' + '#' * 80)
print('ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ')
print('#' * 80)

print('\n' + '=' * 70)
print('ЗАДАЧА 1. Сортировка пузырьком')
print('Условие: Задание. Используя словесное и визуальное описание, реализовать сортировку пузырьком.')
numbers = [5.0, 1.0, 4.0, 2.0, 2.0]
print('Входные данные:')
print('Массив:', numbers)
print('Результат:')
task_01(numbers)

print('\n' + '=' * 70)
print('ЗАДАЧА 2. Сортировка вставками')
print('Условие: Задание. Используя словесное и визуальное описание, реализовать сортировку вставками.')
numbers = [5.0, 1.0, 4.0, 2.0, 2.0]
print('Входные данные:')
print('Массив:', numbers)
print('Результат:')
task_02(numbers)

print('\n' + '=' * 70)
print('ЗАДАЧА 3. Сортировка выбором')
print('Условие: Задание. Используя словесное и визуальное описание, реализовать сортировку выбором.')
numbers = [5.0, 1.0, 4.0, 2.0, 2.0]
print('Входные данные:')
print('Массив:', numbers)
print('Результат:')
task_03(numbers)

print('\n' + '=' * 70)
print('ЗАДАЧА 4. Бинарный поиск')
print('Условие: Задание. Используя словесное описание, реализовать бинарный поиск.')
numbers = [1.0, 3.0, 3.0, 7.0, 9.0]
target = 3.0
print('Входные данные:')
print('Массив:', numbers)
print('target =', target)
print('Результат:')
task_04(numbers, target)

print('\n' + '=' * 70)
print('ЗАДАЧА 5. Дерево: структура, поиск и симметричный обход')
print('Условие: Задание. Используя словесное описание, реализовать обход дерева.')
values = [4.0, 2.0, 6.0, 1.0, 3.0, 5.0, 7.0]
target = 3.0
print('Входные данные:')
print('Порядок вставки в дерево:', values)
print('Искомое число:', target)
print('Результат:')
task_05(values, target)

print('\n' + '=' * 70)
print('ЗАДАЧА 6. Очередь')
print('Условие: Задание. Используя словесное описание, реализовать работу с очередью.')
print('Входные данные: добавить 10 и 20, показать очередь, извлечь оба элемента.')
print('Результат:')
queue = Queue()
queue.enqueue(10)
print('Добавлен элемент: 10')
queue.enqueue(20)
print('Добавлен элемент: 20')
print('Очередь:', *queue.show())
print('Первый элемент:', queue.peek())
print('Размер очереди:', queue.size())
print('Извлечён элемент:', queue.dequeue())
print('Очередь после извлечения:', *queue.show())
print('Извлечён элемент:', queue.dequeue())
print('Очередь пуста:', queue.is_empty())
