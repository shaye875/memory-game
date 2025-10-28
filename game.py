from board import *
def init_game(size1,size2,name,max_turn):
    board = init_board(size1,size2)
    cards = init_cards(size1,size2)
    cards = mixing(cards)
    i1 = -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            i1+=1
            board[i][j] = cards[i1]
    return {"name":name,"board":board,"sum_cards_won":"","sum_cards_lost":0,"max_turns":max_turn}

def is_was(state,x1,y1,x2,y2):

    if state["board"][x1][y1] in state["sum_cards_won"]:
        print("its was chois agein")
        return True
    return False

def is_rigth(state,card1x,card1y,card2x,card2y):

    if state["board"][card1x][card1y] == state["board"][card2x][card2y]:
               state["sum_cards_won"]+=state["board"][card1x][card1y]
               print("yes you good mor choich")
               return True
    print("now yry agein")
    state["sum_cards_lost"]+=1
    return False

def print_chice(state,x1,y1,x2,y2):
    str = ""
    for i in range(len(state["board"])):
        if i > 0:
            str+="\n"
        for j in range(len(state["board"][i])):
            if i == x1 and j == y1:
                str+=state["board"][i][j]
            elif i == x2 and j == y2:
                str+=state["board"][i][j]
            else:
                str+="x"
    print(str)

def is_won(state):
    count = 0
    for i in range(len(state["board"])):
        for j in range(len(state["board"][i])):
            count+=1
    if len(state["sum_cards_won"]) == (count//2) and state["max_turns"] > state["sum_cards_lost"]:
        return True


    return False

def is_lost(state):
    if state["sum_cards_lost"] > state["max_turns"]:
        return True
    return False

def print_matrix(state):
    str = ""
    for i in range(len(state["board"])):
        if i > 0:
            str += "\n"
        for j in range(len(state["board"][i])):
            if state["board"][i][j] in state["sum_cards_won"]:
                str+=state["board"][i][j]
            else:
                str+="x"
    return str

def print_status(state):
    print(f"now you ahve more {state["max_turns"]-state["sum_cards_lost"]} \n you hit at {state["sum_cards_won"]}\n you lost{state["sum_cards_lost"]}")

def print_end(state):
    print(f"now the summary is: {state["name"]} you card do you win{state["sum_cards_won"]}\n sum cards do you lost {state["sum_cards_lost"]} \n the map is {print_board(state["board"])}\n by by")
