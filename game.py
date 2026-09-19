import random,time
'''a= random.randint(1000,9999)

for i in range(5):
    print(random.randint(1000,9999))
    time.sleep(2)
    '''
def rock_paper_scissors():
    count=3
    player_score=0
    bot_score=0
    while count>0:
        print('\nWELCOME TO ROCK PAPER SCISSOR')
        print('='*30)
        player=input('<-- Enter one of these -- > \nRock ,paper,scissors: ').lower().strip()
        bot=random.choice(["rock","paper","scissors"])
        print('bot: ',bot)

        if player==bot:
            print('Tie')
        elif player== 'paper' and bot=='rock':
            print('you won')
            player_score+=1
        elif player== 'rock' and bot=='scissors':
            print('you won')
            player_score+=1

        elif player== 'scissors' and bot=='paper':
            print('you won')
            player_score+=1

        else:
            print('bot won')
            bot_score+=1
        count-=1
        print('your score:',player_score)
    print(f'GAME OVER \nYour score: {player_score} \nBot score: {bot_score}')

    if bot_score > player_score:
        print('Bot won , Better luck next time')
    else:
        print('You won !')

def guess_number():
    print('WELCOME TO GUESS A NUMBER')
    player=int(input('Enter a number between 1-10 (Inclusive): '))
    bot=random.randint(1,10)
    print('Bot number:',bot)
    if player==bot:
        print("You won! IMPRESSIVE !")
    else:
        print('Better luck next time ')


print('CHOOSE ONE OF THESE(1,2,3): \n1) Rock-Paper-Scissors \n2) Guess a Number \n3) Go and Study')
choice=input().strip()

if choice=='1':
    rock_paper_scissors()
elif choice=='2':
    guess_number()
elif choice=='3':
    print('Nice job ! ')
else:
    print('READ the instructions clearly Mr.Stupid')





