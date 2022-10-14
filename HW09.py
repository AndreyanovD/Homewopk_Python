# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

data = open('file.txt', 'w')
data.write('1\n2\n6\n7')
data.close()
number = int(input('Введите число: '))
list = []
for i in range(-number, number + 1):
    list.append(i)
print(list)
mult = 1
data = open('file.txt', 'r')
for line in data:
    mult *= int(list[int(line)])
print('Произведение элементов равно ', mult)
data.close()
