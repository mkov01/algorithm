def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # 120

# Дополнительно Итерационная версия факториала:
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))

# Сравнивание: 
import time
import sys

def measure_time_and_memory(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    memory = sys.getsizeof(func(n))
    return end_time - start_time, memory

time_recursive, memory_recursive = measure_time_and_memory(factorial_recursive, 1000)
time_iterative, memory_iterative = measure_time_and_memory(factorial_iterative, 1000)

print(f"Рекурсивная версия: Время: {time_recursive:.6f}s, Память: {memory_recursive} байт")
print(f"Итеративная версия: Время: {time_iterative:.6f}s, Память: {memory_iterative} байт")