import random
def init_board(size1,size2):
    board = []
    for i in range(size1):
        board.append([])
        for j in range(size2):
            board[i].append("")
    return board

def init_cards(size1,size2):
    cards = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","V","w","Y","x","z"]
    cards1 = []
    for i in range((size1*size2)//2):
        cards1.append(cards[i])
        cards1.append(cards[i])
    return cards1

def mixing(cards):
    for _ in range(1000):
        i1 = random.randint(0, len(cards) - 1)
        i2 = random.randint(0, len(cards) - 1)
        cards[i2],cards[i1] = cards[i1],cards[i2]
    return cards

def print_board(board):
    str = ""
    for i in range(len(board)):
        str+="\n"
        for j in range(len(board[i])):
            str+=board[i][j]
    return str

