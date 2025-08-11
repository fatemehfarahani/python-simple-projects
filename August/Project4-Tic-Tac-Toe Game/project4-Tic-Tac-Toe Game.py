import numpy as np 
import random
import time


board=np.array([

    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']


])

print(board)


def check_main_diagonal(board , player):

    return np.all(np.diag(board) == player)


def check_sub_diagonal(board , player):
    
    return  np.all(np.diag(np.fliplr(board))== player )



def check_row(board, player):

    for row in range (board.shape[0]):

        if np.all(board[row, :] == player):

            return True
        
    return False



def check_column( board , player):

    for column in range( board.shape[1]):

        if np.all(board[: , column] == player):
             
            return True
        
    return False


def has_empty_cell(board):

    return np.any((board !='X') & (board != 'O'))


def computer_move(board,player):

    empty_cells=[]

    for row in range(3):
        for col in range(3):

            if board[row,col] not in ['X' ,'O']:

                empty_cells.append((row,col))
                       
   

        for (row,col) in empty_cells:

            temp_board = board.copy()  
            temp_board[row,col] = 'X'

            if check_row(temp_board, 'X') or check_column(temp_board,'X') or check_main_diagonal(temp_board,'X') or check_sub_diagonal(temp_board, 'X'):
                return (row , col)


        for (row,col) in empty_cells:

            temp_board = board.copy()  
            temp_board[row,col] = player

            if check_row(temp_board, player) or check_column(temp_board,player) or check_main_diagonal(temp_board,player) or check_sub_diagonal(temp_board, player):
                return (row , col)  


    return random.choice(empty_cells)




player='X'

while True:

    try:

        if player =='X':
            user_input=int(input(f"player {player} chose a cell from table:"))
            
            
            if  1 <= user_input <=9 :

                row=(user_input-1)//3
                col=(user_input-1) %3
                    
                if board[row,col] == str(user_input):
                    
                    board[row,col] = player

                    print(board ,'\n')
            

                    if check_main_diagonal(board,player) or check_sub_diagonal(board, player) or check_row(board, player) or check_column(board, player):
                        print(f"PLAYER {player} WINS!")
                        break

                    elif not has_empty_cell (board):

                        print("Game ended in a draw!")
                        break
                        
                    
                    player ='O'
                    print(f'player {player} is thinking...\n')
                    row,col = computer_move(board, player)
                    board[row,col]= player
                    time.sleep(2)
                    print(board,'\n')
                    

                    if check_main_diagonal(board,player) or check_sub_diagonal(board, player) or check_row(board, player) or check_column(board, player):
                        print(f"PLAYER {player} WINS!")
                        break

                    elif not has_empty_cell (board):

                        print("Game ended in a draw!")
                        break
                    
                    
                    player = 'X'

                else:
                    print('cell taken! please select another one.')

            
            else:
                print('The number shold be between 1 and 9!Try again.')   
                                

    except:

        print('You shold enter a number! Tray again.')

    
         