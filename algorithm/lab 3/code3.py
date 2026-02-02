score = int(input("Введите число от 1 до 100: "))

if score < 1 or score > 100:
    print("Ошибка: число должно быть в диапазоне от 1 до 100")
elif 90 <= score <= 100:
    print("Оценка: A")
elif 75 <= score <= 89:
    print("Оценка: B")
elif 60 <= score <= 74:
    print("Оценка: C")
else:
    print("Оценка: D")