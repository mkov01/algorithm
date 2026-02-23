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