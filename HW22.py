# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

def input_data(player):
    x = int(input(f'{player}, введите количество конфет от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{player}, введите правильное количество конфет (от 1 до 28): '))
    return x

def print_turn(player, n, candy_sum, candy_value):
    print(f'{player} взял {n} конфет, теперь у него {candy_sum}. На столе осталось {candy_value} конфет.')

def bot_input(c_value, player_input):
    win_value = 29
    if (c_value - (win_value - player_input)) % 29 == 0:
        step = win_value - player_input
    else:
        step = c_value % win_value
    if step == 0:
        step = randint(1, 29)
    if step > c_value:
        step = c_value    
    return step
    
bot_init = False
if input('Вы хотите сыграть с ботом? Y/N ').upper() == 'Y':
    bot_init = True
   
player1 = "Игрок 1"
if bot_init:
    player2 = "Бот"
else:
    player2 = "Игрок 2"

candy_value = 221
if bot_init:
    turn = 1
else:    
    turn = randint(0,2)
counter_1 = 0
counter_2 = 0
candies = 0

if turn:
    print(f'Первый ходит {player1}.')
else:
    print(f'Первый ходит {player2}.')

while candy_value > 0:
    if turn:
        candies = input_data(player1)
        counter_1 += candies
        candy_value -= candies
        turn = False
        print_turn(player1, candies, counter_1, candy_value)
    elif not bot_init:
        candies = input_data(player2)
        counter_2 += candies
        candy_value -= candies
        turn = True
        print_turn(player2, candies, counter_2, candy_value)
    else:
        candies_bot = bot_input(candy_value, candies)
        counter_2 += candies_bot
        candy_value -= candies_bot
        turn = True
        print_turn(player2, candies_bot, counter_2, candy_value)

if not turn:
    print(f'Победил {player1}!')
else:
    print(f'Победил {player2}!')