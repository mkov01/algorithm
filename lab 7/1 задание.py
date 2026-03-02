def add(a, b):
    return a + b

def power(a, n=2):
    return a ** n

def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total
result_add = add(5 , 3)
print(f"Сумма 5 и 3: {result_add}")

result_power = power(4)
print(f"4 в квадрате: {result_power}")

result_sum = sum_all(1, 2, 3, 4, 5)
print(f"Сумма всех чисел: {result_sum}")