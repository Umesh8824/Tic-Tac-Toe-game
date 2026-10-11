def make_board(size):
    row = []
    for i in range(size):
        row += ' '
    board = []
    for x in range(size):
        board += [row.copy()]
    return board

def format_board(board):
    m = [] 
    sep = '\n  '+ "-+" * (len(board) - 1) + '-' + '\n'
    u = []
    for i in range(len(board)):
        u += [str(i + 1)]
    for i in range(len(board)):
        row = board[i]
        line = str(i+1) + ' ' + '|'.join(row)
        m += [line]
    return '  ' + ' '.join(u) + '\n' + sep.join(m)

def play_move(board, player):
    size = len(board)
    while True:
        row = int(input('Enter row no: ')) - 1
        col = int(input('Enter column no: ')) -1
        if row < 0 or row >= size or col < 0 or col >= size:
            print("That position is off the bord. Try again")
        elif board[row][col] != ' ':
            print('This Position is alredy taken. Try again')
        else:
            board[row][col] = player
            return

def row_winner(board):
    for row in board:
        Winner = True
        for i in row:
            if i != row[0] or i == ' ':
                Winner = False
                break
        if Winner:
            return True
    return False

def column_winner(board):
    size = len(board)
    for col in range(size):
        Winner = True
        for row in range(size):
            if board[row][col] != board[0][col] or board[row][col] == ' ':
                Winner = False
                break
        if Winner:
            return True
    return False

def diagonal_winner(board):
    size = len(board)
    Winner = True
    for row in range(size):
        for col in range(size):
            if row == col:
                if board[row][col] != board[0][0] or board[row][col] == ' ':
                    Winner = False
                    break
    if Winner:
        return True
    Winner = True
    for row in range(size):
        for col in range(size):
            if row + col == size -1:
                if board[row][col] != board[0][size-1] or board[row][col] == ' ':
                    Winner = False
                    break
    if Winner:
        return True
    return False

def has_winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game(size):
    board = make_board(size)
    player = 'X'
    while True:
        print(format_board(board))
        print((f"Players{player}'s turn"))
        play_move(board, player)

        if has_winner(board):
            print(format_board(board))
            print(f"Player {player} wins!")
            break

        if board_full(board):
            print(format_board(board))
            print(f"it's a draw!")
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

size = int(input('Enter board size: '))
play_game(size)
