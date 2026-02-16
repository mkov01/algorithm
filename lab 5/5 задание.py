n = int(input("Введите количество элементов: "))
while n <= 0:
    print("n должно быть больше 0")
    n = int(input("Введите количество элементов: "))
a = []
for i in range(n):
    x = int(input("Введите число: "))
    a.append(x)
if n < 2:
    print("Невозможно найти второй по величине элемент")
else:
    max1 = a[0]
    max2 = a[0]
    for i in range(n):
        if a[i] > max1:
            max1 = a[i]
    max2 = None
    for i in range(n):
        if a[i] != max1:
            if max2 is None or a[i] > max2:
                max2 = a[i]
    if max2 is None:
        print("В массиве все элементы равны")
    else:
        print("Второй по величине элемент:", max2)