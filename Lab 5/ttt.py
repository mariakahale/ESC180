'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def square_num_to_coord(square_num):
    if square_num==1:
        square_num =  [0,0]
    if square_num==2:
        square_num =  [0,1]
    if square_num==3:
        square_num =  [0,2]
    if square_num==4:
        square_num =  [1,0]
    if square_num==5:
        square_num =  [1,1]
    if square_num==6:
        square_num =  [1,2]
    if square_num==7:
        square_num =  [2,0]
    if square_num==8:
        square_num =  [2,1]
    if square_num==9:
        square_num =  [2,2]
    return square_num
    
def put_in_board(board, mark, square_num):
    board[square_num[0]][square_num[1]] = mark 
    return board

def get_mark():
    turn = 0
    game_over= False
    while not game_over :
        while turn %2 == 0 and not game_over:
            square_num = int(input("Player X, enter number:"))
            print_board_and_legend(put_in_board(board, "X", square_num_to_coord(square_num)))
            if is_win(board,"X") == True or is_win(board,"O") == True:
                print("Player X has won")
                game_over = True 
            turn +=1
        while turn %2 != 0 and not game_over:
            square_num = int(input("Player O, enter number:"))
            print_board_and_legend(put_in_board(board, "O", square_num_to_coord(square_num)))
            if is_win(board,"X") == True or is_win(board,"O") == True:
                print("Player O has won")
                game_over = True

             
            turn +=1

def get_free_squares(board):
    free_squares_list = []
    for i in range(0, len(board)):
        for j in range(0,2):
            if board[i][j]==" ":
                free_squares_list.append([i, j])
    return free_squares_list

def make_random_move(board, mark):

    while not is_win(board, mark):
        free_squares_list = get_free_squares(board)
        options = len(free_squares_list)
        computer_choice = random.randint(0, options-1)
        computer_coord = free_squares_list[computer_choice]
        put_in_board(board, mark, computer_coord)
        if not is_win(board, mark):
            put_in_board(board, " ", computer_coord)
        if is_win(board, mark):
            return 


def is_row_all_marks(board, row_i, mark):
    if board[row_i][0]==mark and board[row_i][1] == mark and board[row_i][2] == mark:
        return True
def is_col_all_marks(board, col_i, mark):
    if board[0][col_i]==mark and board[1][col_i]==mark and board[2][col_i]==mark:
        return True
def is_diagonal_all_marks(board, mark):
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == mark:
        return True

def is_win(board, mark):
    for row_i in range(0,3):
        if is_row_all_marks(board, row_i, mark):
            return True
    for col_i in range(0,3):
        if is_col_all_marks(board, col_i, mark):
            return True
    if is_diagonal_all_marks(board, mark):
        return True



if __name__ == '__main__':

    board = make_empty_board()
    
    print("\n\n")
    
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    
    print_board_and_legend(board)

    get_mark()


