word = "algorithm"
char_dict = {}

for char in word:
    char_dict[char] = char_dict.get(char, 0) + 1

print(char_dict)