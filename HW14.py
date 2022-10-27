# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите число: '))
digit_number = 0
digit = 1
while number > 0:
    digit_number += (number % 2) * digit
    number = number // 2
    digit *= 10

print('Это число в двоичной системе равно', digit_number)
