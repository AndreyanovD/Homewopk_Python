# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

data_1 = open('file_1.txt', 'w')
data_1.write('2*x^4 + 5*x^3 + 1*x^2 + 2*x^1 + 9 = 0')
data_1.close()

data_2 = open('file_2.txt', 'w')
data_2.write('8*x^4 + 7*x^3 + 3*x^2 + 8*x^1 + 7 = 0')
data_2.close()

data_1 = open('file_1.txt', 'r+')
list_data_1 = data_1.read().replace(' = 0', '').split(' + ')

data_2 = open('file_2.txt', 'r+')
list_data_2 = data_2.read().replace(' = 0', '').split(' + ')

print(list_data_1)
print(list_data_2)

dictionary = {}

for i in range(len(list_data_1)):
    if 'x' in list_data_1[i]:
        dictionary[int(list_data_1[i][-1:-2:-1])] = int(list_data_1[i][:1])
    else:
        dictionary[0] = int(list_data_1[i][:])

for i in range(len(list_data_2)):
    if 'x' in list_data_1[i]:
        dictionary[int(list_data_2[i][-1:-2:-1])] += int(list_data_2[i][:1])
    else:    
        dictionary[0] += int(list_data_2[i][:])

print(dictionary)

with open('file_result.txt', 'w+') as result:
    for i in range (max(dictionary.keys()), 0, -1):
        result.write(f'{dictionary[i]}*x^{i} + ')
    result.write(f'{dictionary[0]} = 0')

res = ''                                            # 
for i in range (max(dictionary.keys()), 0, -1):     #
    res += f'{dictionary[i]}*x^{i} + '              #
                                                    # Это просто для проверки
res += f'{dictionary[0]} = 0'                       #
                                                    #
print(res)                                          #