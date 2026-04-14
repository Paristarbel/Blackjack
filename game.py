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
            print(f"Computer's first card: {computer}")

            choose_card=input("Type 'y' to get another card,type 'n' to pass :").lower()
            if choose_card =='y':
                #For player
                for i in range(length):
                    if i == 3:
                        i+=1
                        player.append(cards[i])
                        print(f"Your final hand :{player} , final score {sum(player)}")
                #Computer 
                sum_computer=sum(computer)
                for i in range(len(computer)):
                    if i == 3 :
                        continue
                    elif i==4:
                        i+=1
                        computer.append(cards[i])
                        print(f"Computer's hand :{computer} , final score {sum(computer)}")
                
                
            if choose_card =="n":
                print(f"Your final hand :{player} , final score {sum(player)}")
                sum_computer=sum(computer)
                for i in range(len(cards)):
                    if  i==3  :
                        i+=1
                        computer.append(cards[i])
                print(f"Computer final hand :{computer} , final score {sum(computer)}")
                

                # if sum(player) < sum(computer):
                #     print("Opponent went over ,you WIN🌟✊😭")
shuffle_cards()