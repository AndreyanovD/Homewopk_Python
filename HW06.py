# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

number = input('Введите число: ')
number = number.replace(',','')
number = number.replace('.','')
sum = 0
if number.isdigit():
    for i in range(len(number)):
        sum += int(number[i])
    print('Сумма цифр числа равна', sum)
else:
    print('Число введено неправильно')