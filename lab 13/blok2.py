#ВОПРОС № 6
import math

def task_6_nested_loops(n):
    print("--- Задача 6: Вложенные циклы (O(n^2)) ---")
    count = 0
    # Внутренний цикл идет до i
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            count += 1
    print(f"При n = {n}, количество итераций: {count}")
    print(f"Формула n(n+1)/2: {n}*({n}+1)/2 = {int(n*(n+1)/2)}\n")

def task_10_sieve(n):
    print("--- Задача 10: Решето Эратосфена (O(n log log n)) ---")
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
    result = [i for i, val in enumerate(primes) if val]
    print(f"Простые числа до {n}: {result}\n")

def task_duplicates_comparison(arr):
    print("--- Задача: Поиск дубликатов (O(n log n)) ---")
    # Сортировка занимает O(n log n)
    arr.sort()
    duplicates = []
    # Линейный проход O(n)
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            duplicates.append(arr[i])
    print(f"Найденные дубликаты: {list(set(duplicates))}\n")

def task_matrix_mult(n):
    print("--- Задача: Умножение матриц (O(n^3)) ---")
    # Создаем две матрицы n x n
    matrix_a = [[1 for _ in range(n)] for _ in range(n)]
    matrix_b = [[1 for _ in range(n)] for _ in range(n)]
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    # Три вложенных цикла
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    print(f"Матрица {n}x{n} успешно перемножена (условно {n**3} операций).\n")

def task_log_loop(n):
    print("--- Задача: Логарифмический цикл (O(log n)) ---")
    i = 1
    steps = 0
    while i <= n:
        steps += 1
        print(f"Шаг {steps}: i = {i}")
        i *= 2
    print(f"Итого шагов для n={n}: {steps} (что равно округленному log2({n}))\n")

if __name__ == "__main__":
    # Запуск всех демонстраций
    task_6_nested_loops(10)
    task_10_sieve(30)
    task_duplicates_comparison([4, 2, 7, 2, 1, 9, 4])
    task_matrix_mult(30) # n=30 дает 27,000 операций
    task_log_loop(100)
    
    input("Нажмите Enter, чтобы выйти...")