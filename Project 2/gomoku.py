"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 28, 2022
"""
#part a
def is_sq_on_board(board,y,x):
    if 0<= y < len(board) and 0<= x<len(board[0]):
        return True
    return False

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    # print("yend, xend", y_end, x_end)
    conditions = [True,True] #stores information on whether it is blocked on either the start or end, respectively
    #first checks the ends of the sequence
    if is_sq_on_board(board,y_end,x_end) and (y_end == len(board) or x_end == len(board)) :
        conditions[1]=False
    elif is_sq_on_board(board,y_end,x_end) and ( y_end <0 or x_end<0):
        conditions[0]=False

    #next, checks the following spaces 
    if y_end+d_y >= len(board) or x_end + d_x >= len(board) or y_end + d_y < 0 or x_end+d_x<0:
        conditions[1]= False #sets the end clause to be false because it is blocked or end of board met.

    elif board[y_end + d_y][x_end + d_x] != " ":
        conditions[1]= False 


    #looks at start of sequence
    if (x_end-d_x*length) < 0 or (y_end-d_y*length) < 0 or (x_end-d_x*length) >=len(board) or (y_end-d_y*length) >=len(board):
        conditions[0]=False
    elif board[y_end-d_y*length][x_end-d_x*length] != " ":
        conditions[0]=False

    #culmination
    if conditions[0] == False and conditions[1]==False:
        return "CLOSED"
    elif conditions[0] == False or conditions[1] == False:
        return "SEMIOPEN"
    else:
        return "OPEN"

def sequence_len(board, col, y_start, x_start, d_y, d_x):
    counter=1    
    if board[y_start][x_start] != col:
        return 0
    for i in range(len(board)):
        if not is_sq_on_board(board, y_start+d_y, x_start+d_x):
            return counter
        elif  board[y_start+d_y][x_start+d_x]!=col:
            return counter
        counter += 1
        y_start += d_y
        x_start += d_x

#part b
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    
    big_coord = [y_start,x_start]
    counter = 0
    open_seq_count,semi_open_seq_count=0,0
    tracker = 0

    while 0<=big_coord[0]<len(board) and 0<=big_coord[1]<len(board) and tracker<=len(board): #while we are remaining on the board
        if board[big_coord[0]][big_coord[1]] == col:

            counter = sequence_len(board, col, big_coord[0], big_coord[1], d_y, d_x)
            if length == counter:

                if is_bounded(board, big_coord[0]+(length-1)*d_y, big_coord[1]+(length-1)*d_x,length,d_y, d_x) == "OPEN":
                    open_seq_count += 1
                if is_bounded(board, big_coord[0]+(length-1)*d_y, big_coord[1]+(length-1)*d_x,length,d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1
                
                big_coord = [big_coord[0] +(length-1)*d_y, big_coord[1]+(length - 1)*d_x]
                
            else:
                
                big_coord[0] += (counter - 1) * d_y
                big_coord[1] += (counter - 1) * d_x
        big_coord = [big_coord[0]+d_y, big_coord[1]+d_x]

        tracker+=1


    return open_seq_count, semi_open_seq_count

def detect_row_win(board, col, y_start, x_start, length, d_y, d_x):
    big_coord = [y_start,x_start]
    counter = 0
    open_seq_count,semi_open_seq_count,closed_seq_count=0,0,0
    tracker = 0

    while 0<=big_coord[0]<len(board) and 0<=big_coord[1]<len(board) and tracker<=len(board): #while we are remaining on the board
        if board[big_coord[0]][big_coord[1]] == col:

            counter = sequence_len(board, col, big_coord[0], big_coord[1], d_y, d_x)
            if length == counter:

                if is_bounded(board, big_coord[0]+(length-1)*d_y, big_coord[1]+(length-1)*d_x,length,d_y, d_x) == "OPEN":
                    open_seq_count += 1
                if is_bounded(board, big_coord[0]+(length-1)*d_y, big_coord[1]+(length-1)*d_x,length,d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1
                if is_bounded(board, big_coord[0]+(length-1)*d_y, big_coord[1]+(length-1)*d_x,length,d_y, d_x) == "CLOSED":
                    closed_seq_count += 1
                
                big_coord = [big_coord[0] +(length-1)*d_y, big_coord[1]+(length - 1)*d_x]
                
            else:
                
                big_coord[0] += (counter - 1) * d_y
                big_coord[1] += (counter - 1) * d_x
        big_coord = [big_coord[0]+d_y, big_coord[1]+d_x]

        tracker+=1

    return open_seq_count, semi_open_seq_count, closed_seq_count

def detect_rows_win(board, col, length):
    open_seq_count, semi_open_seq_count,closed_seq_count = 0, 0,0
    semi_open = ()

    #checks for when (dy, dx) = (0,1)
    for column in range(len(board[0])):
        # print("column", column)
        semi_open = detect_row_win(board, col, 0, column, length, 1,0)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        closed_seq_count += semi_open[2]
        # print("column", column, "open", open_seq_count, "semi", semi_open_seq_count)


    #checks for when (dy, dx) = (1,0)
    for r in range(len(board[0])):
        # print("row", r)
        semi_open = detect_row_win(board, col, r, 0, length, 0, 1)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        closed_seq_count += semi_open[2]
        # print("row", r, "open", open_seq_count, "semi", semi_open_seq_count)

    #checks for when (dy,dx) = (1,1), think of it like upper triangle
    for row in range(0,len(board)):
        semi_open = detect_row_win(board, col, row, 0, length, 1, 1)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        closed_seq_count += semi_open[2]


        # print("1,1", "row",row, "open", open_seq_count, "semi", semi_open_seq_count)     
    for column in range(1,len(board)-1):
        semi_open = detect_row_win(board, col, 0, column, length, 1, 1)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]    
        closed_seq_count += semi_open[2]

        # print("1,1", "clmn",column, "open", open_seq_count, "semi", semi_open_seq_count)     

    #checks for when (dy,dx) = (1,-1)
    for row in range(1,len(board)-1):
        semi_open = detect_row_win(board, col, row, len(board)-1, length, 1, -1)
        # if row==0:
            # print("JADED", detect_row(board, col, row, len(board)-1, length, 1, -1))
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        closed_seq_count += semi_open[2]
        # print("1,-1", "row",row, "open", open_seq_count, "semi", semi_open_seq_count)     

    for column in range(0,len(board)):
        semi_open = detect_row_win(board, col, 0, column, length, 1, -1)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        closed_seq_count += semi_open[2]

        # print("1,-1", "clms", column, "open", open_seq_count, "semi", semi_open_seq_count)     

    return open_seq_count, semi_open_seq_count, closed_seq_count

def is_empty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] != " ":
                return False
    return True
    
    
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    semi_open = ()

    #checks for when (dy, dx) = (0,1)
    for column in range(len(board[0])):
        # print("column", column)
        semi_open = detect_row(board, col, 0, column, length, 1,0)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        # print("column", column, "open", open_seq_count, "semi", semi_open_seq_count)


    #checks for when (dy, dx) = (1,0)
    for r in range(len(board[0])):
        # print("row", r)
        semi_open = detect_row(board, col, r, 0, length, 0, 1)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        # print("row", r, "open", open_seq_count, "semi", semi_open_seq_count)

    #checks for when (dy,dx) = (1,1), think of it like upper triangle
    for row in range(0,len(board)):
        semi_open = detect_row(board, col, row, 0, length, 1, 1)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        # print("1,1", "row",row, "open", open_seq_count, "semi", semi_open_seq_count)     
    for column in range(1,len(board)-1):
        semi_open = detect_row(board, col, 0, column, length, 1, 1)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]    

        # print("1,1", "clmn",column, "open", open_seq_count, "semi", semi_open_seq_count)     

    #checks for when (dy,dx) = (1,-1)
    for row in range(1,len(board)-1):
        semi_open = detect_row(board, col, row, len(board)-1, length, 1, -1)
        # if row==0:
            # print("JADED", detect_row(board, col, row, len(board)-1, length, 1, -1))
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]
        # print("1,-1", "row",row, "open", open_seq_count, "semi", semi_open_seq_count)     

    for column in range(0,len(board)):
        semi_open = detect_row(board, col, 0, column, length, 1, -1)
        open_seq_count+= semi_open[0]
        semi_open_seq_count += semi_open[1]

        # print("1,-1", "clms", column, "open", open_seq_count, "semi", semi_open_seq_count)     

    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    max_score = [-100000, "y", "x"]
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == " ":
                board[row][column] = "b"

                if score(board) > max_score[0]:
                    max_score = [score(board), row, column]
                board[row][column] = " "
    if max_score[0]!=-100000:
        move_y, move_x = max_score[1], max_score[2]
    else:
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == " ":
                    move_y = row 
                    move_x = column
    return move_y, move_x
    
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


    
def is_win(board):
    #checks if full
    is_full = True
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == " ":
                is_full = False

    if (detect_rows_win(board,"w",5))[0] >0 or (detect_rows_win(board,"w",5))[1] >0 or (detect_rows_win(board,"w",5))[2] >0:
        return "White won"
    elif (detect_rows_win(board,"b",5))[0] >0 or (detect_rows_win(board,"b",5))[1] >0 or (detect_rows_win(board,"b",5))[2] >0:
        return "Black won"
    elif is_full:
        return "Draw"
    else:
        return "Continue playing"

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)   

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
              
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board=[['w', 'w', ' ', ' ', 'b', 'b', 'b', 'b'], ['b', 'b', 'w', 'w', 'w', 'w', 'w', ' '], [' ', 'b', ' ', 'b', ' ', 'w', 'b', ' '], [' ', 'b', 'w', ' ', 'b', 'b', 'b', ' '], [' ', 'w', 'w', ' ', ' ', 'w', 'b', ' '], ['b', 'b', 'w', ' ', ' ', ' ', 'w', 'b'], ['b', 'b', ' ', 'w', 'w', ' ', ' ', 'b'], [' ', ' ', 'w', ' ', 'w', 'b', ' ', 'w']]

    print_board(board)
    if detect_row(board, "b", 0,1,2,1,0) == (0,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board=[['w', 'w', ' ', ' ', 'b', 'b', 'b', 'b'], ['b', 'b', 'w', 'w', 'w', 'w', 'w', ' '], [' ', 'b', ' ', 'b', ' ', 'w', 'b', ' '], [' ', 'b', 'w', ' ', 'b', 'b', 'b', ' '], [' ', 'w', 'w', ' ', ' ', 'w', 'b', ' '], ['b', 'b', 'w', ' ', ' ', ' ', 'w', 'b'], ['b', 'b', ' ', 'w', 'w', ' ', ' ', 'b'], [' ', ' ', 'w', ' ', 'w', 'b', ' ', 'w']]

    print_board(board)
    if detect_rows(board, "b",2) == (2,3):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = [[' ', 'w', 'b', 'w', 'b', ' ', 'b', ' '], ['w', 'w', 'b', 'b', 'w', 'b', 'w', 'b'], ['b', 'b', 'w', ' ', ' ', ' ', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'w', 'w'], [' ', 'b', 'b', 'b', ' ', 'w', ' ', ' '], ['b', ' ', 'w', ' ', 'b', 'b', 'w', 'b'], ['b', 'w', ' ', ' ', 'w', 'b', 'w', 'w'], ['b', 'b', 'b', ' ', 'w', ' ', 'w', ' ']]

    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED", search_max(board))

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    
    test_search_max()