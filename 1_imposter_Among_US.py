#Guessing One Imposter AMONG US

import random
import time
players1={
        1: "NARAYAN" ,
        2: "LOUIS"  ,
        3: "RAJAT" ,
        4: "PANKAJ" ,
        5: "RITIK",
        6: "HARISH"  ,
        7: "VISHESH" ,
        8: "SIDDHANT"  ,
        9: "NISHANT",
        10: "NITIN"  ,
        }
players={
        "NARAYAN"   : 1,
        "LOUIS"    : 2,
        "RAJAT"   : 3,
        "PANKAJ"   : 4,
        "RITIK"  : 5,
        "HARISH"    : 6,
        "VISHESH"  : 7,
        "SIDDHANT"    : 8,
        "NISHANT"  : 9,
        "NITIN"     : 10,
        }

while True:
    fails=0
    players_copy = players.copy()
    players1_copy= players1.copy()
    a=random.randint(1,10)
    imposter=players1[a]
    print("-"*80)
    print("You have to find out the IMPOSTER in 3 chances...\n \nLets go....")
    print('*'*80)
    input("Press 'ENTER' to start the game. . .")
    for turns in range(3):
        players_name="\n".join(players1_copy.values())
        print('"'*80)
        guess = input("Vote Who Would be the Imposter among these...\n"+players_name+"\n").upper()
        if guess in players_name:
            del_player=players[guess]
            print("Ejecting {} ".format(guess))
            for i in range(3):
                print(".")
                time.sleep(1)
            if guess in imposter:
                del players1_copy[del_player]
                print("\nYes {} was the IMPOSTER : 0 IMPOSTERS REMAINING ".format(guess))
                break
            else:
                print("-"*80)
                del players1_copy[del_player]
                print("{} was not an Imposter".format(guess))
            print("-"*80)
            fails+=1
        else:
            print("Choose one of these player..",end="\n")
            break
    if fails==3:
        print("{} was the IMPOSTER".format(imposter))
        print("-"*80)
        choice=input("Do you still Wanna Play \n choose your option --- ('Y' -> PLAY AGIAN / 'N' -> QUIT)..").upper()
        if choice == 'N':
            print("Have a nice day " )
            break
    else:
        choice=input("Do you still Wanna Play \n choose your option --- ('Y' -> PLAY AGIAN / 'N' -> QUIT)..").upper()
        if choice == 'N':
            print("Have a nice day " )
            break
        print("\nYou the best..")
        break   
