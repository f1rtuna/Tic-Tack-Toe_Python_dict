theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M':  ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def see_winner(board):
    won_or_not = False
    #rows X
    if (board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X') or (board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X') \
        or (board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X'):
        print('X has won!')
        won_or_not = True

    #diagonals X
    if (board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X') or (board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X'):
        print('X has won!')
        won_or_not = True

    #columns X
    if (board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X') or (board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X') \
        or (board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X'):
        print('X has won!')
        won_or_not = True
    
    #rows Y
    if (board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O') or (board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O') \
        or (board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O'):
        print('O has won!')
        won_or_not = True

    #diagonals Y
    if (board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O') or (board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O'):
        print('O has won!')
        won_or_not = True

    #columns Y
    if (board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O') or (board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O') \
        or (board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == 'O'):
        print('O has won!')
        won_or_not = True
    return won_or_not


turn = 'X'
game_won = False
game_count = 0
print('Welcomd to a simple Python Game utilizing dictionary key values as moves!')
print('=========================================================================')
print('Here are the moves:')
print('-------------------------------------------------------------------------')
for keys in theBoard:
    print(keys + ' ', end = '')
print()
print('-------------------------------------------------------------------------')
print('K lets START')
print('=========================================================================')
while(not game_won and game_count < 9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    game_count += 1
    game_won = see_winner(theBoard)
    print()

if(game_count == 9):
    print('It wa a tie :(')

printBoard(theBoard)