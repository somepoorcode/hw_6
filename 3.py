try:
    with open('kids.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Файл kids.txt не найден")
    exit(1)

youngest_age = float('inf')
oldest_age = 0

youngest_child = None
oldest_child = None

for line in lines:
    parts = line.split()
    if len(parts) == 3:
        last_name, first_name, age = parts
        age = int(age)
        if age < youngest_age:
            youngest_age = age
            youngest_child = (last_name, first_name, age)
        if age > oldest_age:
            oldest_age = age
            oldest_child = (last_name, first_name, age)

with open('youngest.txt', 'w') as file:
    file.write(f'{youngest_child[0]} {youngest_child[1]} {youngest_child[2]}\n')

with open('oldest.txt', 'w') as file:
    file.write(f'{oldest_child[0]} {oldest_child[1]} {oldest_child[2]}\n')
