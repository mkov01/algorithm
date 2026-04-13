#ВОПРОС № 1
import time
import numpy as np
import matplotlib.pyplot as plt

# 1. Реализация линейного поиска
def linear_search(arr, target):
    """Проходит по каждому элементу массива."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 2. Реализация бинарного поиска
def binary_search(arr, target):
    """Ищет элемент в отсортированном массиве, деля его пополам."""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def run_experiment():
    # Набор размеров массива от 100 до 1 000 000
    sizes = [100, 1000, 5000, 10000, 50000, 100000, 250000, 500000, 750000, 1000000]
    linear_times = []
    binary_times = []

    print(f"{'Size':>10} | {'Linear (s)':>12} | {'Binary (s)':>12}")
    print("-" * 40)

    for n in sizes:
        # Создаем отсортированный массив
        test_array = np.arange(n)
        # Ищем число, которого нет в массиве, чтобы проверить "худший случай"
        target = -1 
        
        # Замер времени для линейного поиска
        start_linear = time.perf_counter()
        linear_search(test_array, target)
        end_linear = time.perf_counter()
        linear_duration = end_linear - start_linear
        linear_times.append(linear_duration)
        
        # Замер времени для бинарного поиска
        start_binary = time.perf_counter()
        binary_search(test_array, target)
        end_binary = time.perf_counter()
        binary_duration = end_binary - start_binary
        binary_times.append(binary_duration)
        
        print(f"{n:10d} | {linear_duration:12.8f} | {binary_duration:12.8f}")

    # 3. Визуализация результатов
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, label='Linear Search O(n)', marker='o', color='red')
    plt.plot(sizes, binary_times, label='Binary Search O(log n)', marker='s', color='blue')
    
    plt.title('Comparison of Linear and Binary Search Time Complexity')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)  
    print("\nПостроение графика...")
    plt.show()

if __name__ == "__main__":
    run_experiment()