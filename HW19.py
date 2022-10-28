# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

from random import randint

degree = int(input('Введите степень многочлена: '))

data = open('file.txt', 'w')
for i in range(degree+1):
    if i != degree:
        data.write(f'{randint(0,100)}*x^{degree-i} + ')
    else:
        data.write(f'{randint(0,100)} = 0')
data.close()