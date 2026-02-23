import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

print("\nСформированный массив:")
for row in matrix:
    for element in row:
        print(f"{element:4}", end="")
    print()

total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element

print("\nСумма всех элементов:", total_sum)

print("\nСумма элементов каждой строки:")
row_sums = []
for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Строка {i + 1}: {row_sum}")

print("\nСумма элементов каждого столбца:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Столбец {j + 1}: {col_sum}")

max_sum = max(row_sums)
max_index = row_sums.index(max_sum)

print(f"\nСтрока с максимальной суммой: {max_index + 1}")
print(f"Максимальная сумма: {max_sum}")
