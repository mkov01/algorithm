n = int(input("Введите натуральное число n: "))

count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
        count += 1

print("\nКоличество чётных чисел:", count)
