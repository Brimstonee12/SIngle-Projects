import random
import time

print('\n')
print("---------------------------------WELCOME TO ROCK ,PAPER AND SCISSORS GAME! HAVE FUN!!---------------------------------")
time.sleep(3)
rounds = 1
gracz = 0
komp = 0
while rounds < 7:
    print("Round",rounds,'!')
    player = input('Paper,Rock or Scissors?: ')
    comp = random.choice(['Paper','Rock','Scissor'])
    print("Computer Generated :", comp)
    if player == comp:
        rounds +=1
        print("Draw")
    elif player == 'Paper' and comp =='Rock':
        rounds +=1
        gracz +=1
        print("Paper Wins!")
    elif player=='Rock' and comp=='Paper':
        rounds +=1
        komp +=1
        print("Paper Wins!")
    elif player == 'Paper' and comp =='Scissors':
        rounds +=1
        komp +=1
        print("Scissors Wins!")
    elif player=='Scissors' and comp=='Paper':
        rounds +=1
        gracz +=1
        print("Scissors Wins!")
    elif player == 'Rock' and comp =='Scissors':
        rounds +=1
        gracz+=1
        print("Rock Wins!")
    elif player=='Scissors' and comp=='Rock':
        rounds +=1
        komp +=1
        print("Rock Wins!")
    else:
        print("Write Correctly")
    print('\n')
print('\n')
print("Scores:")
print("Player:",gracz,'Computer:',komp)
if gracz > komp:
    print('You Won!')
elif komp > gracz:
    print("You Lose!")
else:
    print("Draw!!")
