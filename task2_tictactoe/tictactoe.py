# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def make_move(position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_winner('O'): return 1
    if check_winner('X'): return -1
    if check_draw(): return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# The Game Loop
while True:
    print_board()
    
    # Human turn
    try:
        pos = int(input("Choose your position (0-8): "))
        if make_move(pos, 'X'):
            if check_winner('X'): 
                print_board()
                print("You win!"); break
        else:
            print("Invalid move!"); continue
    except ValueError:
        print("Please enter a number between 0 and 8."); continue

    # AI turn
    if not check_draw():
        ai_pos = best_move()
        make_move(ai_pos, 'O')
        if check_winner('O'): 
            print_board()
            print("AI wins!"); break
    else:
        print_board()
        print("It's a draw!"); break

    
