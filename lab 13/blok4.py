#ВОПРОС № 18
import sys

def analyze_sparse_matrix():
    # Параметры матрицы 1000x1000
    rows, cols = 1000, 1000
    
    print(f"--- Задача 18: Анализ памяти (Матрица {rows}x{cols}) ---\n")

    # 1. Двумерный массив (Список списков)
    # Инициализируем матрицу, где заполнено всего 5 элементов (0.0005% заполнения)
    dense_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    dense_matrix[1][1] = 10
    dense_matrix[500][500] = 20
    
    # Считаем примерный вес (объекты Python тяжелее сырых массивов C++)
    dense_size = sys.getsizeof(dense_matrix) + sum(sys.getsizeof(row) for row in dense_matrix)
    # Добавляем вес самих целых чисел (примерно)
    dense_size += (rows * cols) * 28 # 28 байт на объект int в Python
    
    print(f"1. Стандартный двумерный массив:")
    print(f"   Затраты памяти: ~{dense_size / 1024 / 1024:.2f} МБ")
    print(f"   Сложность доступа: O(1)\n")

    # 2. Список ненулевых элементов (Разреженная матрица через словарь)
    # Храним только те индексы, где значение не равно нулю: {(r, c): value}
    sparse_matrix = {
        (1, 1): 10,
        (500, 500): 20,
        (999, 999): 30,
        (123, 456): 40,
        (888, 111): 50
    }
    
    # Вес словаря зависит от количества ключей
    sparse_size = sys.getsizeof(sparse_matrix)
    # Добавляем вес ключей (кортежей) и значений
    for key, value in sparse_matrix.items():
        sparse_size += sys.getsizeof(key) + sys.getsizeof(value)

    print(f"2. Разреженная матрица (Dictionary-based):")
    print(f"   Количество элементов: {len(sparse_matrix)}")
    print(f"   Затраты памяти: ~{sparse_size / 1024:.2f} КБ")
    print(f"   Сложность поиска: O(1) в среднем (хэш-таблица)\n")

    # Вывод
    ratio = dense_size / sparse_size
    print(f"ИТОГ: Разреженная матрица эффективнее в {int(ratio)} раз(а) для данного случая.")

if __name__ == "__main__":
    analyze_sparse_matrix()
    input("\nНажмите Enter, чтобы выйти...")