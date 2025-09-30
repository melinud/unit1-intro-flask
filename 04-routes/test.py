def winning_move(board, player):
    """Check if there's a winning move for the player and return the position"""
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  #Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  #Vertical
        [0, 4, 8], [2, 4, 6]              #Diagonal
    ]
    for combo in winning_combos:
        values = [board[i] for i in combo]
        if values.count(player) == 2 and values.count('') == 1:
            return combo[values.index('')]
    return None

def ai_move(board, ai='O', human='X'):
    # 1 win if possible
    m = winning_move(board, ai)
    if m is not None:
        return m
    # 2 block opponent
    m = winning_move(board, human)
    if m is not None:
        return m
    # 3 simple heuristic
    # Take center asap
    if board[4] == '':
        return 4
    # First he takes the open corners
    corners = [0, 2, 6, 8]
    available_corners = [i for i in corners if board[i] == ''] #Empty cells
    if available_corners:
        return available_corners[0]
    # If there are none left then the edges
    edges = [1, 3, 5, 7]
    available_edges = [i for i in edges if board[i] == '']
    if available_edges:
        return available_edges[0]
    # Then anything else
    for i in range(9):
        if board[i] == '':
            return i

def check_winner(board):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  #Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  #Vertical
        [0, 4, 8], [2, 4, 6]              #Diagonal
    ]
    
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    
    if '' not in board:
        return 'Tie'
    return None

def display(board):
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(' | '.join([cell if cell != '' else str(i+j) for j, cell in enumerate(row)]))
        if i < 6:
            print('---------')

def play_game():
    board = [''] * 9
    current_player = 'X'  # Human goes first
    print("Welcome")
    print("You are X, AI is O")
    print("Enter position (0-8): ")
    display(board)
    print()

    while True:
        if current_player == 'X':  # Human turn
            try:
                move = int(input(f"Your move (0-8): "))
                if board[move] != '':
                    print("Position already taken!")
                    continue
                board[move] = 'X'
            except (ValueError, IndexError):
                print("Invalid input")
                continue
        else:
            # AI turn
            move = ai_move(board)
            board[move] = 'O'
            print(f"AI chooses position {move}")
        
        display(board)
        print()
        
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()