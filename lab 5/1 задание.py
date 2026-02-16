while True:
    n = int(input("Введите количество элементов (n > 0): "))
    if n > 0:
        break
    else:
        print("Ошибка! n должно быть больше 0.")

arr = []

for i in range(n):
    num = int(input(f"Введите элемент {i + 1}: "))
    arr.append(num)

print("Полученный массив:", arr)
