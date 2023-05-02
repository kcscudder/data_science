from random import random, randrange
from secrets import randbelow, randbits

def DrawTest1():

    player_2 = randrange(1, 53)

    print(player_1)

    def SuitPlayer1():
        if player_1 <= 13 :
            print("clubs")
        elif player_1 > 13 and player_1 <= 26 :
            print("diamonds")
        elif player_1 > 26 and player_1 <= 40 :
            print("hearts")
        else :
            print("diamonds")

    def FacePlayer1():
        if player_1 < 9 :
            print(player_1 + 1)
        elif player_1 >= 14 and player_1 <= 22 :
            print(player_1 + 1)
        elif player_1 >= 27 and player_1 <= 35 :
            print(player_1 + 1)
        elif player_1 >= 40 and player_1 <= 48 :
            print(player_1 + 1)
        else :
            print("face card")
    
    SuitPlayer1()
    FacePlayer1()

def Draw():
    
    player_1_suit = randrange(1, 5)
    player_1_face = randrange(1, 14)

    print("player 1")
    print(player_1_suit)
    print(player_1_face)

    player_1_key = int(str(player_1_suit) + str(player_1_face)) # generates unique key for player's first card
    print(player_1_key)

    i = 1

    print("player 2")

    while i == 1 :
    
        player_2_suit = randrange(1, 5)
        player_2_face = randrange(1, 14)

        print(player_2_suit)
        print(player_2_face)

        player_2_key = int(str(player_2_suit) + str(player_2_face)) # generates unique key for player's second card
        print(player_2_key)

        if player_2_face != player_1_face: # will re-enter loop if first two card keys are identical, else exit loop
            break

    

Draw()