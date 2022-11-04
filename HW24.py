# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = open('file_rle.txt', 'w')
data.write('qwwwwaaaeeeeerrrrssdrrrhhhhhi')
data.close()

data = open('file_rle.txt', 'r+')
data_str = data.read()
data.close()
new_data = ''
count = 1

for i in range(1, len(data_str)):
    if data_str[i] == data_str[i - 1]:
        count +=1
        if i == len(data_str)-1:
            new_data += data_str[i-1] + f'{count}'
    else:
        new_data += data_str[i-1] + f'{count}'
        count = 1
        if i == len(data_str)-1:
            new_data += data_str[i] + f'{count}'

with open('file_rle_new.txt', 'w+') as result:
    
    result.write(new_data)

unpacked_data = ''
with open('file_rle_new.txt', 'r+') as temp_data:
    new_data = temp_data.read()
    print(new_data)
    for i in range(0, len(new_data)):
        if new_data[i].isalpha():
            symbol = new_data[i]
            count = int(new_data[i+1])
            unpacked_data += symbol * count
