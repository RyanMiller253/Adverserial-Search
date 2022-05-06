import Connect4
import PlayerX
import PlayerO
import copy
import random
from time import sleep

# allows you to watch the game at human speed -- set to 0 for the computer to play quickly.
DELAY = 1.0

""" Function: run_tournament
    Description: Runs two rounds of Connect 4, the first has X move first and the second has O move first.  The 
    moves are delayed by DELAY seconds to allow a human to watch the game in real time.
"""


def run_tournament():
    # Load lookup tables
    lookupX = PlayerX.load_player("X")
    lookupO = PlayerO.load_player("O")

    print("Round 1: X goes first")
    game = Connect4.C4Game()  # create new game board
    game.nextPlayer = 'X'  # X is going first
    r1_winner = False
    while not r1_winner:
        # request a move from X
        move = PlayerX.next_move(copy.deepcopy(game), "X", lookupX)
        # check whether move is legal, and if not, select randomly from among legal moves
        legal_moves = game.available_moves()
        if move not in legal_moves:
            print('random move!')
            move = random.choice(legal_moves)
        # update game board and display
        game.make_move(move)
        print(game, "\n")
        sleep(DELAY)
        # if X didn't just win, proceed to O's move
        r1_winner = game.winner()
        if r1_winner == False:
            # request a move from O
            move = PlayerO.next_move(copy.deepcopy(game), "O", lookupO)
            # check whether move is legal, and if not, select randomly from among legal moves
            legal_moves = game.available_moves()
            if move not in legal_moves:
                move = random.choice(legal_moves)
            # update game board and display
            game.make_move(move)
            print(game, "\n")
            sleep(DELAY)
            # test for winne\            r1_winner = game.winner()
    # winner won't be reported until after round 2, when both sets of results will be reported together

    print("Round 2: O goes first")
    game = Connect4.C4Game()  # create new game board
    game.nextPlayer = 'O'  # this time O moves first
    r2_winner = False
    while not r2_winner:
        # request a move from O
        move = PlayerO.next_move(copy.deepcopy(game), "O", lookupO)
        # check whether move is legal, and if not, select randomly from among legal moves
        legal_moves = game.available_moves()
        if move not in legal_moves:
            move = random.choice(legal_moves)
        # update game board and display
        game.make_move(move)
        print(game, "\n")
        sleep(DELAY)
        r2_winner = game.winner()
        if r2_winner == False:
            # request a move from X
            move = PlayerX.next_move(copy.deepcopy(game), "X", lookupX)
            # check whether move is legal, and if not, select randomly from among legal moves
            legal_moves = game.available_moves()
            if move not in legal_moves:
                move = random.choice(legal_moves)
            # update game board and display
            game.make_move(move)
            print(game, "\n")
            sleep(DELAY)
            r2_winner = game.winner()

    # report both sets of results
    print("Round 1 Winner:", r1_winner)
    print("Round 2 Winner:", r2_winner)


if __name__ == "__main__":
    run_tournament()
