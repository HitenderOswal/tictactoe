"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for line in board:
        for space in line:
            if space == X:
                xcount += 1
            elif space == O:
                ocount += 1
    if xcount <= ocount:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    return action

def result(board1, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board = copy.deepcopy(board1)
    if action in actions(board):
        board[action[0]][action[1]] = player(board)
        return board
    else:
        raise Exception

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    result = utility(board)
    if result == 1:
        return X
    elif result == -1:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) != 0:
        return True
    for line in board:
        for space in line:
            if space == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return 1
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return -1
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return 1
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return -1

    if board[0][0] == board[1][1] == board[2][2] == X:
        return 1
    if board[0][0] == board[1][1] == board[2][2] == O:
        return -1
    if board[0][2] == board[1][1] == board[2][0] == X:
        return 1
    if board[0][2] == board[1][1] == board[2][0] == O:
        return -1

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    bestaction = None
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            step = minvalue(result(board, action))
            if step > v:
                v = step
                bestaction = action
    elif player(board) == O:
        v = math.inf
        for action in actions(board):
            step = maxvalue(result(board, action))
            if step < v:
                v = step
                bestaction = action        
    return bestaction

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v