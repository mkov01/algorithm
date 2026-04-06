numbers = [5, 2, 5, 3, 2, 5]
counts = {}

for n in numbers:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

print(counts)