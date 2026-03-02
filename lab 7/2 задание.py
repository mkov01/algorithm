x = 10

def change_global_variable():
    global x
    print(f"Значение x до изменения (внутри функции): {x}")
    x = 20
    print(f"Значение x после изменения (внутри функции): {x}")

print(f"Значение x до вызова функции: {x}")
change_global_variable()
print(f"Значение x после вызова функции: {x}")