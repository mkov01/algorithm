#ВОПРОС № 11
import time

def fib_recursive(n):
    """Наивная рекурсия со сложностью O(2^n)"""
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    """Итеративный подход со сложностью O(n)"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def run_experiment():
    print("--- Сравнение методов вычисления Фибоначчи ---")
    print(f"{'n':>5} | {'Итеративный (O(n))':>20} | {'Рекурсия (O(2^n))':>20}")
    print("-" * 55)

    # Мы будем увеличивать n, пока рекурсия не станет слишком долгой
    for n in range(5, 101, 5):
        # Замер итеративного метода
        start_iter = time.time()
        res_iter = fib_iterative(n)
        end_iter = time.time()
        time_iter = end_iter - start_iter

        # Замер рекурсивного метода
        if n <= 40:  # После 40 рекурсия обычно начинает "зависать"
            start_rec = time.time()
            res_rec = fib_recursive(n)
            end_rec = time.time()
            time_rec = f"{end_rec - start_rec:.4f} сек"
        else:
            time_rec = "СЛИШКОМ ДОЛГО..."

        print(f"{n:>5} | {time_iter:>19.6f} сек | {time_rec:>20}")
        
        if n == 40:
            print("\n[ВНИМАНИЕ] Рекурсия начинает заметно тормозить...")

if __name__ == "__main__":
    run_experiment()
    print("\nОпыт завершен.")
    input("Нажмите Enter, чтобы закрыть консоль...")