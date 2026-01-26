n = int(input("Натуральное число n: "))

product = 1

for i in range(1, n + 1):
    product = product + i

    print(f"Количество выведенных чисел. {n} равно: {product}")