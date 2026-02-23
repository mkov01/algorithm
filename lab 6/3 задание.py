import random

field = []

for i in range(4):
    row = []
    for j in range(4):
        row.append(random.randint(1, 9))
    field.append(row)

print("Исходное поле:")
for row in field:
    for num in row:
        print(num, end=" ")
    print()

for i in range(4):
    last = field[i][3]   
    
    for j in range(3, 0, -1):
        field[i][j] = field[i][j - 1]
    
    field[i][0] = last   
print("\nПосле сдвига вправо:")
for row in field:
    for num in row:
        print(num, end=" ")
    print()