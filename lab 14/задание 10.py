items = [1, 1, 5, 5, 5, 2, 2, 3]
max_streak = 0
current_streak = 1

for i in range(len(items) - 1):
    if items[i] == items[i+1]:
        current_streak += 1
    else:
        if current_streak > max_streak:
            max_streak = current_streak
        current_streak = 1
# На случай если самая длинная пачка была в конце
max_streak = max(max_streak, current_streak)

print("Длина самой длинной серии:", max_streak)