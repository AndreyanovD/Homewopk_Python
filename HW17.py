# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите натуральное число: '))

mult_list = []

for i in range(2, number//2 + 1):
    if number % i == 0:
        flag = 0
        for j in mult_list:         # проверка на простое число 
            if i % j == 0:
                flag += 1
        if flag == 0:
            mult_list.append(i)

print(mult_list)