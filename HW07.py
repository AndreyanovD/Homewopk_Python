# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N

number = int(input('Введите число: '))
mult = list(range(1, number + 1))
for i in range(2, number + 1):
        mult[i-1] = mult[i-2] * i
print(mult)