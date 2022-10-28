# Вычислить число c заданной точностью

number = float(input('Введите число: '))
accuracy = float(input('Введите нужную точность в формате 0.0001: '))

count = 0

while accuracy != 1:
    count +=1
    accuracy *= 10

print(round(number, count))