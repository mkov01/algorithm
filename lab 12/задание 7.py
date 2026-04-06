shop = {"Молоко": 80, "Хлеб": 45}

shop["Сыр"] = 150
shop["Молоко"] = 85
del shop["Хлеб"]
print(f"Цена сыра: {shop.get('Сыр')}")
print(shop)