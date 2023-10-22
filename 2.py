try:
    with open('input2.txt', 'r') as input_file:
        numbers = [int(line.strip()) for line in input_file]
except FileNotFoundError:
    print("Файл input2.txt не найден")
    exit(1)

if len(numbers) != 10:
    print("Файл input2.txt должен содержать 10 чисел")
    exit(1)

try:
    numbers = [int(num) for num in numbers]
except ValueError:
    print("Файл input2.txt должен содержать только числа")
    exit(1)

sorted_numbers = sorted(numbers, key=lambda x: sum(int(digit) for digit in str(x)))

with open('output2.txt', 'w') as output_file:
    for number in sorted_numbers:
        output_file.write(str(number) + '\n')
