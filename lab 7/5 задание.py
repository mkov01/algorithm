def max_element(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    
    max_rest = max_element(arr, index + 1)
    
    return max(arr[index], max_rest)

arr = [3, 5, 7, 2, 8, 1]
print(max_element(arr))

# Реализация:

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))

# Оптимизация:

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(fibonacci_memo(6))
