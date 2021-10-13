# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:58:19 2020

@author: Paritosh
"""

#Player.py

import math
import random

class Player:
    def __init__(self, letter):
        #Letter initialized as either 'x' or 'o'
        self.letter = letter
        
    #We want all players get their next move in the game
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + " 's turn. Input move (0-8): ")
            #we are going to check that this is a correct value by trying to cast
            # it to an integer, and if it is not then we say it is invalid
            # If that spot is not available on the board then we also it is invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            
            except ValueError:
                print('Invalid Square. Try Again!!')
                
        return val     
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #Randomly Choose One
        else:
            #Get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter #This is us as we want to maximize our score
        other_player = 'O' if player =='X' else 'X'
        # First, we want to check if the previous move is a winner
        # This is our best case
        if state.current_winner == other_player:
            #We should return position and score because we need to keep
            #track of the score for minimax to work
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else (
                            -1 * (state.num_empty_squares() + 1))
                    }
            
        elif not state.empty_squares(): #No empty stones
            return {'position': None, 'score': 0 }
            
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
            #Each scorre should be maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize
            
        for possible_move in state.available_moves():
            
            # Step 1: make a move, try that spot
            state.make_move(possible_move, player)
            
            
            # Step 2: Recurse using minimax to simulate
            # a game after making that move
            sim_score = self.minimax(state, other_player) #Now we alternate player
            
            # Step 3: Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move #Otherwise this will get messed up in recursion part
            
            # Step 4: Update the Dictionaries if necessary
            # If the score is better than what we have at that time, then
            # we will update this weight to keep track of the 
            # best possible move to make
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score #Replace best
            
        return best

            
            
            
            
            
            
            
        
        
        
        
        
            