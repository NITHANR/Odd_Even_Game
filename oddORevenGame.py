from numpy import random

runs=[1,2,3,4,5,6]
player1S=0
player2S=0

print("TOSS!")
print("Select Head as (0) or Tail as (1)",end=" ")
toss=int(input())
player1T=random.choice([0,1])
player2T=random.choice([0,1])

while(True):

    if(player1T==toss and player2T==toss):
        player1T=random.choice([0,1])
        player2T=random.choice([0,1])
    else:
        if(player1T==toss):
            print("Player1 Won the Toss and They will Bat First")
            while(True):
                player1ST=random.choice(runs)
                player2ST=random.choice(runs)
                print(f"Player 1 = {player1ST} and Player 2 = {player2ST}")
                if(player1ST==player2ST):
                    print("Player 1 is out!")
                    print(f"Player 1 Score Total is {player1S}")
                    break
                else:
                    player1S+=player1ST
            print("Now,Player 2 will Bat")
            while(True):
                player2ST=random.choice(runs)
                player1ST=random.choice(runs)
                print(f"Player 2 = {player2ST} and Player 1 = {player1ST}")
                if(player2ST==player1ST):
                    print("Player 2 is Out!")
                    print(f"Player 2 Score Total is {player2S}")
                    break
                else:
                    player2S+=player2ST  
               
        else:
            print("Player2 Won the Toss and They will Bat First")
            while(True):
                player1ST=random.choice(runs)
                player2ST=random.choice(runs)
                print(f"Player 2 = {player2ST} and Player 1 = {player1ST}")
                if(player1ST==player2ST):
                    print("Player 2 is out!")
                    print(f"Player 2 Score Total is {player2S}")
                    break
                else:
                    player2S+=player2ST
            print("Now,Player 1 will Bat")
            while(True):
                player2ST=random.choice(runs)
                player1ST=random.choice(runs)
                print(f"Player 1 = {player1ST} and Player 2 = {player2ST}")
                if(player2ST==player1ST):
                    print("Player 1 is Out!")
                    print(f"Player 1 Score Total is {player1S}")
                    break
                else:
                    player1S+=player1ST 
        
        print("\nMatch is over!!!\n")
        print("SCOREBOARD")
        print(" __________ ____")
        print("|          |    |")
        print(f"| Player 1 | {player1S} |")
        print("|          |    |")
        print(" __________ ____")
        print("|          |    |")
        print(f"| Player 2 | {player2S} |")
        print("|          |    |")
        print(" __________ ____\n")
        if(player1S>player2S):
                print("Player 1 WINS!!!")
        else:
                print("Player 2 WINS!!!")
        break
