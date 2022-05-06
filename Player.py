import copy
import Connect4
import Tournament
import operator

'''
    All bit mapping resources are derived from the following link:
    https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0
'''
# node class for creating tree recursively


class Node(object):
    # member variables for each node
    score = 0
    column = 0
    children = []
    state = []
    row = 6
    position = ''
    # recursive initialization function

    def __init__(self, board, move, depth, player):
        player2 = ''
        self.player = player
        self.column = move
        self.state = board
        self.children = []
        self.row = 5
        self.position
        score = 0
        # alternate player based off of turn
        if player == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        if move != -1:  # conditional so we don't work with initial game state
            # creating boards for each node
            row = 5  # initialize row decrementor
            # while top row is empty and current space is taken
            while board.board[row][move] != '.' and board.board[0][move] == '.':
                row -= 1  # look up one row
            self.state.board[row][move] = 'O'  # assign space an O
        position = getPositionFromBitMap(
            board, player)  # get position for bitstring
        self.position = position  # give node position from above
        if determineWin(position) == True:  # if win condition met
            self.score = 1000  # set score to 1000
        else:
            self.score = calculateScore(position)  # otherwise calculate score

        if depth > 0:  # until final desired depth is met
            for i in range(7):  # loop for creating 7 children
                # recursively build tree while decementing depth and adding to children list of parent node
                self.children.append(
                    Node(copy.deepcopy(board), i, depth-1, player2))
                if len(self.children) > 0:  # for nodes with children
                    score += self.children[i].score  # total scores of children
        if len(self.children) > 0:  # if children present
            # assign current node score decrease score by average of children, so it isnt greedy
            self.score -= score/len(self.children)

# function from link, modified to return position from bit map


def getPositionFromBitMap(board, player):
    position, mask = '', ''
    # Start with right-most column
    for j in range(6, -1, -1):
        # Add 0-bits to sentinel
        mask += '0'
        position += '0'
        # Start with bottom row
        for i in range(0, 6):
            if board.board[i][j] != 0:
                mask += '1'
            else:
                mask += '0'
            if board.board[i][j] == player:
                position += '1'
            else:
                position += '0'
    return int(position, 2)

# function fromlink to determine if four in a row


def determineWin(position):
    # Horizontal check
    m = position & (position >> 7)
    if m & (m >> 14):
        return True
    # Diagonal \
    m = position & (position >> 6)
    if m & (m >> 12):
        return True
    # Diagonal /
    m = position & (position >> 8)
    if m & (m >> 16):
        return True
    # Vertical
    m = position & (position >> 1)
    if m & (m >> 2):
        return True
    # Nothing found
    return False

# modified from link above to determine if there are consecutive tokens, the more consecutive the higher the score


def calculateScore(position):
    score = 0
    # Vertical
    m = position & (position >> 1)
    for i in bin(m):
        if i == '1':
            score += 1
    # Horizontal check
    m = position & (position >> 7)
    for i in bin(m):
        if i == '1':
            score += 1
    # Diagonal \
    m = position & (position >> 6)
    for i in bin(m):
        if i == '1':
            score += 1
    # Diagonal /
    m = position & (position >> 8)
    for i in bin(m):
        if i == '1':
            score += 1
    # Nothing found
    return score

# unused function called in tournament


def load_player(player):
    # insert file reading code here -- whatever is returned by this function will be saved as lookupO and passed into
    # next_move for use when choosing a move.
    return None

# next move called from tournament, returns move


def next_move(board, player, lookup_table):
    # insert code to select move -- until this code is updated, player will play randomly
    # generate root node than recursively builds tree, etc
    root = Node(board, -1, 5, player)
    sortedNodeList = sorted(root.children, key=operator.attrgetter(
        'score'), reverse=False)  # sorted list of second level nodes
    move = sortedNodeList[0].column  # fittest move from list
    return move  # send move to tournament
