nums = [1, 2, 3, 2, 4, 5, 1, 6, 1]
seen = []
dupes = []

for x in nums:
    if x in seen and x not in dupes:
        dupes.append(x)
    seen.append(x)

print("Нашел вот такие дубли:", dupes)