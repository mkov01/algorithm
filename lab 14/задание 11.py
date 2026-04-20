db = {"Админ": 20}

while True:
    cmd = input("\nЧе делаем? (add/find/del/exit): ").lower()
    
    if cmd == "add":
        name = input("Имя: ")
        age = int(input("Возраст: "))
        db[name] = age
        print("Добавили!")
    elif cmd == "find":
        name = input("Кого ищем?: ")
        print(f"Возраст: {db.get(name, 'Нет такого в базе')}")
    elif cmd == "del":
        name = input("Кого удаляем?: ")
        if name in db:
            del db[name]
            print("Удалено.")
        else: print("Его и так нет.")
    elif cmd == "exit":
        break