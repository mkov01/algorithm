age = int(input("Введите ваш возраст: "))

student_card = input("У вас есть студенческий билет? (да/нет): ").strip().lower()

if age < 18 or student_card == "да":
    print("Вы имеете право на льготный тариф")
else:
    print("Вы не имеете право на льготный тариф")