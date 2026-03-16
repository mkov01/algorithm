# Задача 1: Класс узла (Node)
class Node:
    def __init__(self, data):
        self.data = data  # Данные
        self.next = None  # Ссылка на следующий узел

# Задача 2: Класс связного списка
class LinkedList:
    def __init__(self):
        self.head = None  # Изначально список пуст

    # Задача 3: Добавление в начало
    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Задача 4: Добавление в конец
    def push_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Задача 5: Вывод всех элементов
    def print_all(self):
        current = self.head
        while current:
            print(current.data, end=" → " if current.next else "")
            current = current.next
        print()

    # Задача 6: Поиск элемента (True/False)
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Задача 7: Удаление первого элемента
    def pop_front(self):
        if self.head:
            self.head = self.head.next

    # Задача 8: Подсчёт количества элементов
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Задача 10: Разворот списка (реверс)
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Запоминаем следующий
            current.next = prev       # Разворачиваем стрелку
            prev = current            # Двигаемся дальше
            current = next_node
        self.head = prev

# Задача 9: Программа для пользователя
def main():
    list_obj = LinkedList()
    
    print("Введите 5 чисел:")
    for i in range(5):
        val = int(input(f"Число {i+1}: "))
        list_obj.push_back(val) # Добавляем в конец
    
    print("\nВаш список:")
    list_obj.print_all()
    
    print(f"Всего элементов: {list_obj.size()}")
    
    # Пример работы поиска и удаления
    print(f"Есть ли число 10 в списке? {list_obj.search(10)}")

# Запуск программы
if __name__ == "__main__":
    main()