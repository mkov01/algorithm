words = ["cat", "dog", "cat", "bird", "dog", "dog"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

duplicates = [w for w in counts if counts[w] > 1]
print(duplicates)