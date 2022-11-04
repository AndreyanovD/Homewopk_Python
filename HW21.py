# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'asf аыфе абв ждцке еабвуу эенжр ывджпф ррабв варж абвв аб'

my_list = list(filter(lambda x: 'абв' not in x, my_text.split()))

print(' '.join(my_list))
