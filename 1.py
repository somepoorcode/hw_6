try:
    with open('input1.txt', 'r') as input_file:
        numbers = input_file.read().strip().split()
except FileNotFoundError:
    print("Файл input1.txt не найден")
    exit(1)

if len(numbers) != 10:
    print("Файл input1.txt должен содержать 10 чисел")
    exit(1)

try:
    numbers = [int(num) for num in numbers]
except ValueError:
    print("Файл input1.txt должен содержать только числа")
    exit(1)

product = 1
for num in numbers:
    product *= num

with open('output1.txt', 'w') as output_file:
    output_file.write(str(product))
