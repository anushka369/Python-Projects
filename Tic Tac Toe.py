COMPUTER = 1
HUMAN = 2
SIDE = 3
COMPUTERMOVE = 'O'
HUMANMOVE = 'X'

def show_board(board):
    for i in range(SIDE):
        print("\t", end="")
      
        for j in range(SIDE):
            print(board[i][j], end=" ")
          
            if j < SIDE - 1:
                print("|", end=" ")
        print()
      
        if i < SIDE - 1:
            print("\t" + "-" * 9)

def show_instructions():
    print("\nChoose a cell numbered from 1 to 9 as below and play\n")
    print("\t 1 | 2 | 3 ")
    print("\t-----------")
    print("\t 4 | 5 | 6 ")
    print("\t-----------")
    print("\t 7 | 8 | 9 \n")

def initialize():
    board = []
    for i in range(SIDE):
        row = []
      
        for j in range(SIDE):
            row.append('*')
          
        board.append(row)
    return board

def declare_winner(whose_turn):
    if whose_turn == COMPUTER:
        print("COMPUTER has won\n")
      
    else:
        print("HUMAN has won\n")

def row_crossed(board):
    for i in range(SIDE):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '*':
            return True
    return False

def column_crossed(board):
    for i in range(SIDE):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '*':
            return True
    return False

def diagonal_crossed(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '*':
        return True
      
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '*':
        return True
      
    return False

def game_over(board):
    return row_crossed(board) or column_crossed(board) or diagonal_crossed(board)

def minimax(board, depth, is_ai):
    if game_over(board):
        if is_ai:
            return -10 
          
        else:
            return 10
      
    if depth == 9:
        return 0
        
    best_score = -9999 if is_ai else 9999
    for i in range(SIDE):
        for j in range(SIDE):
            if board[i][j] == '*':
                if is_ai:
                    board[i][j] = COMPUTERMOVE 
                  
                else:
                    HUMANMOVE
                  
                score = minimax(board, depth + 1, not is_ai)
                board[i][j] = '*'
              
                if is_ai:
                    best_score = max(best_score, score) 
                  
                else:
                    min(best_score, score)
    return best_score

def best_move(board, move_index):
    best_score = -9999
    x, y = -1, -1
    for i in range(SIDE):
        for j in range(SIDE):
            if board[i][j] == '*':
                board[i][j] = COMPUTERMOVE
                score = minimax(board, move_index + 1, False)
                board[i][j] = '*'
              
                if score > best_score:
                    best_score = score
                    x, y = i, j
    return x, y

def play_tic_tac_toe(whose_turn):
    board = initialize()
    move_index = 0
    show_instructions()
    
    while not game_over(board) and move_index < SIDE * SIDE:
        if whose_turn == COMPUTER:
            x, y = best_move(board, move_index)
            board[x][y] = COMPUTERMOVE
            print(f"COMPUTER has put an {COMPUTERMOVE} in cell {x * 3 + y + 1}\n")
            show_board(board)
            whose_turn = HUMAN
          
        else:
            print("Available positions:", end=" ")
            for i in range(SIDE):
                for j in range(SIDE):
                    if board[i][j] == '*':
                        print(i * 3 + j + 1, end=" ")
            print()

            try:
                n = int(input("Enter the position: ")) - 1
                x, y = divmod(n, SIDE)
              
                if board[x][y] == '*' and 0 <= n < 9:
                    board[x][y] = HUMANMOVE
                    print(f"\nHUMAN has put an {HUMANMOVE} in cell {n + 1}\n")
                    show_board(board)
                    whose_turn = COMPUTER
                  
                else:
                    print("Invalid or occupied position, try again.")
                    continue
                  
            except (ValueError, IndexError):
                print("Invalid input, enter a number between 1-9.")
                continue
        move_index += 1
    
    if not game_over(board) and move_index == SIDE * SIDE:
        print("It's a draw\n")
      
    else:
        declare_winner(COMPUTER if whose_turn == HUMAN else HUMAN)

def main():
    print("\n-------------------- Tic-Tac-Toe --------------------\n")
    while True:
        choice = input("Do you want to start first? (y/n): ").lower()
      
        if choice == 'y':
            play_tic_tac_toe(HUMAN)
          
        elif choice == 'n':
            play_tic_tac_toe(COMPUTER)
          
        else:
            print("Invalid choice")
            continue
          
        if input("Do you want to quit? (y/n): ").lower() == 'y':
            break

if __name__ == "__main__":
    main()
