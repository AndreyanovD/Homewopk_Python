# Реализуйте алгоритм перемешивания списка
 
from random import randint

list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
print(list)
print(len(list))
for i in range(len(list)):
    temp = list[i]
    a = randint(0,len(list)-1)
    list[i] = list[a]
    list[a] = temp
print(list)