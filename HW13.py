# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

my_list = ['1.1', '1.2', '3.1', '5', '10.01']

new_list = []

for i, elem in enumerate(my_list):
    new_list.append(round(float(elem) % 1, 2))

max_value = new_list[0]
min_value = new_list[0]

for i in new_list:
    if max_value < i:
        max_value = i
    if min_value > i and i !=0:
        min_value = i

print('Разница между максимальным и минимальным значением дробных частей элементов массива равна', max_value - min_value)
