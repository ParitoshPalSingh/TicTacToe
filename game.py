# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:58:09 2020

@author: Paritosh
"""
import time
from player import HumanPlayer,RandomComputerPlayer, GeniusComputerPlayer

#Game.py
class TicTacToe:
    
    def __init__(self):
        #We will use single list to rep 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None #Keep Track of winnerr!
        
     
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3]  for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    '''
        def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    '''
               
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc
        #Tells us what nu,ber corrosponds to what box 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def available_moves(self):
        #Cleaner way 
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        
        #Alternate way for writing the same thing
        '''moves = []
        for (i,spot) in enumerate(self.board):
            # ['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]
            if spot == ' ':
                moves.append(i)
        return moves
        '''
        
    #Matched Everything till here    
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        #return len(self.available_moves())
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # If valid move, then make the move (assign square to letter) 
        # then return true, if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #Winner if 3 in a row or column or diagonal
        row_ind = square//3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        #Check Column
        col_ind = square%3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #Check Diagonal
        #0,2,4,6,8 - available diagonal elements
        if square %2 ==0 :
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        #If all above are false then this is the end
        return False
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    #Starting Letter    
    letter = 'X'
    #Iterate while the game still has empty squares
    # We dont have to worry about the winner because we will just return that
    # which breaks the loop
    
    while game.empty_squares():
        #pass
        #After we made our move we need to alternate letters
            
        if letter == 'O':
            #square = o_player.get_move(game)
            square = o_player.get_move(game)
        else:
            #square = x_player.get_move(game)
            square = x_player.get_move(game)
            
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square} ')
                game.print_board()
                print('') #Just empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!!')
                return letter
            
            letter = 'O' if letter == 'X' else 'X'  #Switches Player
            #if letter =='X':
                #letter = 'O'
            #else:
                #letter = 'X'
        #inducing a delay
        time.sleep(0.8)
            
    if print_game:
        print("It's a tie ");
        
if __name__ == '__main__':
    
        x_player = HumanPlayer('X')
        #o_player = RandomComputerPlayer('O')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe() #Instance of the TicTacToe
        play(t, x_player, o_player, print_game=True)
        
        