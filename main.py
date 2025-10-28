from board import *
from game import *
def play(name,size1,size2,max_turn):
    state = init_game(size1,size2,name,max_turn)
    while True:
        while True:
          end = False
          print(print_matrix(state))
          x1 = int(input("choise card 1 x-y x:"))
          y1 = int(input("y:"))
          x2 = int(input("choice anuther card x-y x:"))
          y2 = int(input("y:"))
          if x1 == x2 and y1 == y2:
              print("now choich agein")
              continue
          was = is_was(state,x1-1,y1-1,x2-1,y2-1)
          if was == True:
              continue
          print_chice(state,x1-1,y1-1,x2-1,y2-1)
          rigth = is_rigth(state,x1-1,y1-1,x2-1,y2-1)
          if rigth == True:
              win = is_won(state)
              if win == True:
                  print("yes you win the game")
                  print_end(state)
                  end = True
                  break
              print_status(state)
              continue
          print_status(state)
          state["max_turns"]-=1
          break
        if end:
            break
        los = is_lost(state)
        if los == True:
            print("you los the game")
            print_end(state)
            break
if __name__ == "__main__":
    name = input("enter your name")
    size1 = int(input("chohch whou many line do you want"))
    size2 = int(input("choich whu many columns do you want"))
    max_turn = int(input("enter hwu many turns do you want"))
    play(name,size1,size2,max_turn)