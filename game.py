import random

def shuffle_cards():
    is_running=True
    
    try:
        while is_running:
            
            choice= input("Do you want to play a game of Black Jack (y or n)?").lower()
            choice=choice.lower()
        
            if choice == "n":
                is_running=False
                print("Goodbye✌️")
                print("Too bad you are missing all the fun!!")
            elif  choice == "y":
            
                cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
                random.shuffle(cards)
                length=len(cards)
                
                player=cards[0:2]
                computer=cards[2:4]
                
                print(f"Your cards :{player}, current score {sum(player)}")
                print(f"Computer's first card: {[computer[0]]}")

                
                next_card=4
                if sum(player)>21 or sum(computer)>21:
                        is_running = False
                if sum(player)<=21 or sum(computer)<=21:
                    choose_card=input("Type 'y' to get another card,type 'n' to pass :").lower()

                
                if choose_card =='y':

                    #For player
                    while(sum(player)<17):
                        if sum(player)==21 and len(player)==2:
                            return 0
                        if 11 in player and sum(player)>=21:
                            player.remove(11)
                            player.append(1)
                
                        player.append(cards[next_card])
                        next_card+=1
                        
                        if(sum(player)>=21):
                            break
                    #For Computer
                    while(sum(computer) !=0 and sum(computer)<17):
                        if sum(computer)==21 and len(computer)==2:
                            return 0
                        if 11 in computer and sum(computer)>=21:
                            computer.remove(11)
                            computer.append(1)
                        computer.append(cards[next_card])
                        next_card+=1
                        if sum(computer)>17:
                            break
                    print(f"Your final hand :{player} , final score {sum(player)}")
                    print(f"Computer final hand :{computer} , final score {sum(computer)}")
                        
                    is_running = False
                

                    
                if choose_card =="n":

                    
                    # if no then you must leave your player like that ,print their previous value of cards 
                    print(f"Your final hand :{player} , final score {sum(player)}")

                    computer.append(cards[next_card])
                    next_card+=1
                    print(f"Computer final hand :{computer}, final score {sum(computer)}")
                    is_running=False
                
                if sum(player) >21:
                    print("You went over ,You lose😞")
                elif sum(computer) >21:
                    print("You win😭")
                elif sum(player) > sum(computer):
                    print("You WIN🌟✊😭")

                elif sum(computer)>sum(player) :
                    print("You LOSE😞")
                else:
                    print("Draww✊")
    except KeyboardInterrupt:
        print(" ")

shuffle_cards()

Second_game=input("Do you want to play again? (y or n): ").lower()

while(Second_game=="y"):
    shuffle_cards()
