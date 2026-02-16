n = int(input("Введите количество элементов: "))

while n <= 0:
    print("n должно быть больше 0")
    n = int(input("Введите количество элементов: "))

a = []
for i in range(n):
    x = int(input("Введите число: "))
    a.append(x)

pos = 0
neg = 0
even = 0

for i in range(n):
    if a[i] > 0:
        pos = pos + 1
    if a[i] < 0:
        neg = neg + 1
    if a[i] % 2 == 0:
        even = even + 1

print("Количество положительных:", pos)
print("Количество отрицательных:", neg)
print("Количество четных:", even)