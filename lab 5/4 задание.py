n = int(input("Введите количество элементов: "))
while n <= 0:
    print("n должно быть больше 0")
    n = int(input("Введите количество элементов: "))
a = []
for i in range(n):
    x = int(input("Введите число: "))
    a.append(x)
k = int(input("Введите число для поиска: "))
found = False
index = -1
for i in range(n):
    if a[i] == k:
        found = True
        index = i
        break
if found:
    print("Число найдено. Индекс:", index)
else:
    print("Число не найдено в массиве")