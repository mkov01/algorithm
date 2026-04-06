str1 = "listen"
str2 = "silent"

def check_anagram(s1, s2):
    d = {}
    for char in s1: d[char] = d.get(char, 0) + 1
    for char in s2: d[char] = d.get(char, 0) - 1

    return all(value == 0 for value in d.values())

print(check_anagram(str1, str2))