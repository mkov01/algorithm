def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))

# Тестирование:

print(sum_digits(1234))
print(sum_digits(5678))
print(sum_digits(1))
print(sum_digits(0))

# Дополнительные замечания:

def sum_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)