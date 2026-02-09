n = int(input("Введите число n: "))

x = 0
for i in range(1, n + 1):
    x += i

print("Сумма чисел от 1 до", n, "равна", x)