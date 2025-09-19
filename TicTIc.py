board = [' ' for _ in range(9)]

def display_board(board):
    
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_move(player_mark, board):
    
    while True:
        try:
            position = int(input(f"Player {player_mark}, enter your move (1-9): ")) - 1
            if 0 <= position < 9 and board[position] == ' ':
                board[position] = player_mark
                break
            else:
                print("Invalid move. That position is already taken or out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board, player_mark):
    
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for combo in winning_combinations:
        if all(board[i] == player_mark for i in combo):
            return True
    return False

def check_draw(board):
    
    return ' ' not in board

def play_game():
    
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)
        player_move(current_player, board)

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()