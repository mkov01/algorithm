num_input = input("Целое число: ")
number = int(num_input)

if number % 3 == 0 and number % 5 == 0:
    print(f"Число {number} делится и на 3, и на 5.")
elif number % 3 == 0:
    print(f"Число {number} делится на 3, но не на 5.")
elif number % 5 == 0:
    print(f"Число {number} делится на 5, но не на 3.")
else:
    print(f"Число {number} не делится ни на 3, ни на 5.")