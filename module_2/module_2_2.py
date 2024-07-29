first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

print('Решение 1:')
num_set = set()
num_set.add(first)
num_set.add(second)
num_set.add(third)

if len(num_set) == 1:
    print(3)
elif len(num_set) == 2:
    print(2)
else:
    print(0)

print('Решение 2:')
if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)

    