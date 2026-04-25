import random
def shuffle_cards():
    is_running=True

    while is_running:
        
        choice= input("Do you want to play a game of Black Jack (y or n)?")
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
            print(cards)
            print(f"Your cards :{player}, current score {sum(player)}")
            print(f"Computer's first card: {[computer[0]]}")

            choose_card=input("Type 'y' to get another card,type 'n' to pass :").lower()

            next_card=4

            if choose_card =='y':
                #For player

                if sum(player)==21 and len(player)==2:
                    return 0
                if 11 in player and sum(player)>=21:
                    return 0
           
                player.append(cards[next_card])
                next_card+=1
                print(f"Your final hand :{player} , final score {sum(player)}")

                #For Computer
                if sum(computer)==21 and len(computer)==2:
                    return 0
                if 11 in computer and sum(computer)>=21:
                    computer.remove(11)
                    computer.append(1)
                computer.append(cards[next_card])
                next_card+=1
                print(f"Computer final hand :{computer} , final score {sum(computer)}")

                
            if choose_card =="n":

            

                # if no then you must leave your player like that ,print their previous value of cards 
                print(f"Your final hand :{player} , final score {sum(player)}")


                computer.append(cards[next_card])
                next_card+=1
                print(f"Computer final hand :{computer} , final score {sum(computer)}")
                is_running=False

    if sum(computer)>sum(player) :
        print("You went over ,you  LOSE😞")

    if sum(player) > sum(computer):
        print("Opponent went over ,you WIN🌟✊😭")
    if sum(player) == sum(computer):
        print("Draww✊")

shuffle_cards()