# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

sequence = input('Введите последовательность чисел через пробел: ').split()
new_sequence = [sequence[0]]
print(sequence)

for i in range(1, len(sequence)):
    flag = 0
    for elem in new_sequence:
        if sequence[i] == elem:
            flag += 1
    if flag == 0:
        new_sequence.append(sequence[i])

print(new_sequence)

