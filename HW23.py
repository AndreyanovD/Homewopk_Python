# Создайте программу для игры в "Крестики-нолики".

def field(field_list):
    X = 'X'
    y0 = f'   X1  X2  X3     '
    y1 = f'Y1  {field_list[0]} | {field_list[1]} | {field_list[2]} '
    y1_1 = '   ---+---+---'
    y2 = f'Y2  {field_list[3]} | {field_list[4]} | {field_list[5]} '
    y2_1 = '   ---+---+---'
    y3 = f'Y3  {field_list[6]} | {field_list[7]} | {field_list[8]} '
    print(y0)
    print(y1)
    print(y1_1)
    print(y2)
    print(y2_1)
    print(y3)

def move(data, player):
    x_coord = int(data[1]) - 1
    y_coord = int(data[3]) - 1
    if field_list[x_coord + y_coord*3] == " ":
        if player:
            field_list[x_coord + y_coord*3] = 'O'
        else:
            field_list[x_coord + y_coord*3] = 'X'
    else:
        return 0
    return 1

def win():
    for i in range(0,3):
        if field_list[i * 3] == field_list[i * 3 + 1] == field_list[i * 3 + 2] != ' ':
            return 1
        elif field_list[i] == field_list[i + 3] == field_list[i + 6] != ' ':
            return 1
    if field_list[0] == field_list[4] == field_list[8] != ' ':
        return 1
    if field_list[2] == field_list[4] == field_list[6] != ' ':
        return 1
    return 0

field_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

field(field_list)
data = ""

counter = 0

while counter < 9:
    player = counter % 2
    data = input(f'Ход игрока {player + 1}. введите координату в формате x1y2: ')
    check = move(data, player)
    if check:
        field(field_list)
        counter +=1
    else:
        print('Эта ячейка занята.')
    if win():
        print(f'Победил игрок {player + 1}!')
        break

if counter == 9:
    print(f'Ничья :(')
