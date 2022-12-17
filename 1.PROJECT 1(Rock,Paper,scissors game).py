import time
def Game_Process(you,comp):
    if you==comp:
        return None
    
    elif you=='r':
        if comp=='p':
            return 'lost'
        elif comp=='s':
            return 'won'

    elif you=='s':
        if comp=='p':
            return 'won'
        elif comp=='r':
            return 'lost'

    elif you=='p':
        if comp=='s':
            return 'lost'
        elif comp=='r':
            return 'won'
    
from random import *
print(f'**********WELCOME TO THE GAME**********')
print('GAME RULES:\n Rock="r"\n Paper="p"\n Scissor="s"\n You should chose any one of the above\n')
print("if you want to exit the game type e as your choice.After you exit the game your points and computer points are calculated and the final winner will be displayed.")
print("---------------------------------------------------------------------")

print("**********THE GAME STARTS NOW**********")
print('\n')
your_points,comp_points=0,0

while(1):
    RandNo=randint(1,3)
    if RandNo==1:
        comp='r'
    elif RandNo==2:
        comp='p'
    elif RandNo==3:
        comp='s'
    print("computer has chosen it's turn.Now it's your turn")
    you=input('enter your choice:')
    
    
    if you=='e':
        print("**********game has been ended**********")
        print('\n')
        
        break
    
    x=Game_Process(you,comp)
    
    print(f"you have chosen {you}")
    print(f"computer has chosen {comp}")
    
    print("********* ITERATION RESULT *********")
    if(x=='won'):
        print('you have won the game')
        your_points=your_points+1
    elif(x=='lost'):
        print('you have lost the game')
        comp_points=comp_points+1
    elif(x==None):
        print('no one has gained points')
    print('\n')
print("your total score and winner of the game are being calculated,please wait.........")
time.sleep(5)
print("********* GAME RESULT *********")
print(f'your_points={your_points}\ncomp_points={comp_points}\n')
if your_points>comp_points:
    print("**********CONGRATULATIONS!!!,YOU HAVE WON THE GAME**********")
elif your_points<comp_points:
    print("**********COMPUTER HAS WON THE GAME**********")
else:
    print("**********THE GAME IS TIE**********")    
print("---------------------------------------------------------------------")    
