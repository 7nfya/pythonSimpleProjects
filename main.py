from random import randint as r
empty = '-'
feild = [empty for i in range(9)]
def show_feild():
    print(f"""
{feild[0]}    |   {feild[1]}    |   {feild[2]}
{feild[3]}    |   {feild[4]}    |   {feild[5]}
{feild[6]}    |   {feild[7]}    |   {feild[8]}
""")

def winner():
    if feild[0]==feild[1]==feild[2] == 'x' or feild[3]==feild[4]==feild[5] =='x'  or feild[6]==feild[7]==feild[8] =='x' or feild[0]==feild[3]==feild[6] == 'x' or feild[1]==feild[4]==feild[7]=='x' or feild[2]==feild[5]==feild[8]=='x' or feild[0]==feild[4]==feild[8]=='x' or feild[2]==feild[4]==feild[6]=='x':
        return 'x'
    if feild[0]==feild[1]==feild[2 ] == 'o' or feild[3]==feild[4]==feild[5] =='o'  or feild[6]==feild[7]==feild[8] =='o' or feild[0]==feild[3]==feild[6] == 'o' or feild[1]==feild[4]==feild[7]=='o' or feild[2]==feild[5]==feild[8]=='o' or feild[0]==feild[4]==feild[8]=='o' or feild[2]==feild[4]==feild[6]=='o':
        return 'o'
    tie = 0
    for i in feild:
        if i!=empty:
            tie +=1
    if tie == 9:
        return 'tie'
def clear():
    roll = 0
    for i in range(0,9):
        feild[i] = empty
def play_again():
    while True:
        inp = input('wanna play again? (y/n)').lower()
        if inp =='y':
            return True
        elif inp == 'n':
            return False
        else:
            print('invalid input')
    

player = input("type the player's name as X :")
def main_game():
    roll = 0
    while True:
        if winner() == 'x':
            print(f"{player} is the winner !!")
            if play_again():
                print('Have fun !')
                clear()
            else:
                break
        if winner() =='o':
            print('the AI won !')
            if play_again():
                print('Have fun !')
                clear()
            else:
                break
        if winner() == 'tie':
            print('Draw ! Try again')
            if play_again():
                print('Have fun !')
                clear()
            else:
                break
        if roll % 2 == 0:
            while True:
                try:    #X's turn
                    inp = int(input(f"{player}'s turn  (from 1-9)"))
                    if inp in range(1,10):
                        if feild[inp-1] == empty:
                            feild[inp-1] = 'x'
                            roll +=1
                            show_feild() 
                            break
                        else:
                            print('taken feild !')
                    else:
                        print('invalid input')
                except:
                    print('invalid input')
        else:
            if feild[4]==empty:
                feild[4] = 'o'
                roll +=1
                show_feild()
            #horizontally winning feild recognizing
            elif feild[0]==feild[1]=='o' and feild[2] == empty: 
                feild[2] = 'o'
                roll +=1 
                show_feild()
            elif feild[0]==feild[2]=='o' and feild[1] == empty:
                feild[1] = 'o'
                roll +=1 
                show_feild()
            elif feild[1]==feild[2]=='o' and feild[0] == empty:
                feild[0] = 'o'
                roll +=1 
                show_feild()
            elif feild[3]==feild[4]=='o' and feild[5] == empty:
                feild[5] = 'o'
                roll +=1 
                show_feild()
            elif feild[3]==feild[5]=='o' and feild[4] == empty:
                feild[4] = 'o'
                roll +=1 
                show_feild()
            elif feild[4]==feild[5]=='o' and feild[3] == empty:
                feild[3] = 'o'
                roll +=1 
                show_feild()
            elif feild[6]==feild[7]=='o' and feild[8] == empty:
                feild[8] = 'o'
                roll +=1 
                show_feild()
            elif feild[6]==feild[8]=='o' and feild[7] == empty:
                feild[7] = 'o'
                roll +=1 
                show_feild()
            #vertically winning feild recognizing:
            elif feild[0]==feild[3]=='o' and feild[6] == empty:
                feild[6] = 'o'
                roll +=1 
                show_feild()
            elif feild[0]==feild[6]=='o' and feild[3] == empty:
                feild[3] = 'o'
                roll +=1 
                show_feild()
            elif feild[3]==feild[6]=='o' and feild[0] == empty:
                feild[0] = 'o'
                roll +=1 
                show_feild()
            elif feild[1]==feild[4]=='o' and feild[7] == empty:
                feild[7] = 'o'
                roll +=1 
                show_feild()
            elif feild[1]==feild[7]=='o' and feild[4] == empty:
                feild[4] = 'o'
                roll +=1 
                show_feild()
            elif feild[4]==feild[7]=='o' and feild[1] == empty:
                feild[1] = 'o'
                roll +=1 
                show_feild()
            elif feild[2]==feild[5]=='o' and feild[8] == empty:
                feild[8]='o'
                roll +=1 
                show_feild()
            elif feild[2]==feild[8]=='o' and feild[5] == empty:
                feild[5] = 'o'
                roll +=1 
                show_feild()
            elif feild[5]==feild[8]=='o' and feild[2] == empty:
                feild[2] = 'o'
                roll +=1 
                show_feild()
            # diognal moves:
            elif feild[0]==feild[4]=='o' and feild[8] == empty:
                feild[8] = 'o'
                roll +=1 
                show_feild()
            elif feild[0]==feild[8]=='o' and feild[4]==empty:
                feild[4] = 'o'
                roll +=1 
                show_feild()
            elif feild[4]==feild[8]=='o' and feild[0] == empty:
                feild[0] = 'o'
                roll +=1 
                show_feild()
            elif feild[2]==feild[4]=='o' and feild[6]==empty:
                feild[6] = 'o'
                roll +=1 
                show_feild()
            elif feild[2]==feild[6]=='o' and feild[4] == empty:
                feild[4] = 'o'
                roll +=1
                show_feild()
            elif feild[4]==feild[6]=='o' and feild[2] == empty:
                feild[2]='o'
                roll +=1
                show_feild()




            ## blocking X's win movement
            elif feild[0]==feild[1]=='x' and feild[2] == empty:
                feild[2] = 'o'
                roll +=1
                show_feild()
            elif feild[0]==feild[2]=='x' and feild[1]==empty:
                feild[1]='o'
                roll +=1
                show_feild()
            elif feild[1]==feild[2]=='x' and feild[0] == empty:
                feild[0]='o'
                roll +=1
                show_feild()
            elif feild[3]==feild[4]=='x' and feild[5]==empty:
                feild[5]='o'
                roll +=1
                show_feild()
            elif feild[3]==feild[5]=='x' and feild[4] == empty:
                feild[4]='o'
                roll +=1
                show_feild()
            elif feild[4]==feild[5]=='x' and feild[3]==empty:
                feild[3]='o'
                roll +=1
                show_feild()
            elif feild[6]==feild[7]=='x' and feild[8]==empty:
                feild[8] = 'o'
                roll +=1
                show_feild()
            elif feild[6]==feild[8]=='x' and feild[7]==empty:
                feild[7]='o'
                roll +=1
                show_feild()
            elif feild[7]==feild[8]=='x' and feild[6]==empty:
                feild[6]='o'
                roll +=1
                show_feild()
            elif feild[0]==feild[3]=='x' and feild[6]==empty:
                feild[6] ='o'
                roll +=1
                show_feild()
            elif feild[0]==feild[6]=='x' and feild[3] == empty:
                feild[3]='o'
                roll +=1
                show_feild()
            elif feild[3]==feild[6]=='x' and feild[0]==empty:
                feild[0]='o'
                roll +=1
                show_feild()
            elif feild[1]==feild[4]=='x' and feild[7] == empty:
                feild[7]='o'
                roll +=1
                show_feild()
            elif feild[1]==feild[7]=='x' and feild[4] == empty:
                feild[4]='o'
                roll +=1
                show_feild()
            elif feild[4]==feild[7]=='x' and feild[1] == empty:
                feild[1]='o'
                roll +=1
                show_feild()
            elif feild[2]==feild[5]=='x' and feild[8] == empty:
                feild[8]='o'
                roll +=1
                show_feild()
            elif feild[2]==feild[8]=='x' and feild[5] == empty:
                feild[5]='o'
                roll +=1
                show_feild()
            elif feild[5]==feild[8]=='x' and feild[2] == empty:
                feild[2]='o'
                roll +=1    
                show_feild()                                                        
            else:   #random movement if none of the states happened 
                while True:
                    ra= r(0,8)
                    if feild[ra] == empty:
                        feild[ra] = 'o'
                        roll +=1
                        show_feild()
                        break

                     
main_game()