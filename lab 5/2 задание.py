n = int(input("Введите количество элементов: "))

while n <= 0:
    print("n должно быть больше 0")
    n = int(input("Введите количество элементов: "))

a = []
for i in range(n):
    x = int(input("Введите число: "))
    a.append(x)

s = 0
max = a[0]
min = a[0]

for i in range(n):
    s = s + a[i]
    
    if a[i] > max:
        max = a[i]
        
    if a[i] < min:
        min = a[i]

sr = s / n

print("Сумма:", s)
print("Максимум:", max)
print("Минимум:", min)
print("Среднее:", sr)