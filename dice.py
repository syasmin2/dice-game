def dice_game():
    print()
    print ("Welcome To The Casino")
    print()
    print ("At our Casino your credit is good; no up front money is required to")
    print ("play.  When you checkout, we will give you your winnings or you will pay")
    print ("us your losses.  Good luck and enjoy the ride ... ")
    print()
    print ("You must play the game in rounds of 10 plays. If you roll 7 or 11 you will win otherwise you will lose. The odds of rolling a seven is 6 to 1 and the odds of rolling an eleven are 18 to 1.")
    print()
    print ("Press any key to begin playing ")
    print()

    from random import randint

    bankroll = 0
    won_money = 0
    lost_money = 0
    leaving_money = 0

    money_validation = True
    while money_validation :
        bankroll = int(input("How much money you have in your bankroll to play: "))
        if bankroll > 1000:
            print("You cannot enter the casino with more than $1000. Please re-enter: ")
        else:
            money_validation = False

    leaving_money = bankroll           
    continue_playing = "yes"
    while continue_playing == "yes":                
        for i in range(10):
            dice_one = randint(1,6)
            dice_two = randint(1,6)
            customer_roll = dice_one + dice_two            

            bet_validation = True
            while bet_validation :
                bet = int(input("how much money you want to bet: "))
                if bet < 5 or bet > 50:
                    print("You cannot bet less than $5 or more than $50. Please re-enter: ")
                else:
                    bet_validation = False

                print("Your roll: ", customer_roll)

                if customer_roll == 7 :
                    print("Yay! You Won.")
                    won_money = won_money + (bet * 7)
                    leaving_money = leaving_money + (bet * 7)
                elif customer_roll == 11 :
                    print("Yay! You Won.")
                    won_money = won_money + (bet * 19)
                    leaving_money = leaving_money + (bet * 19)
                else:
                    print("Sorry! You Lost.")
                    lost_money = lost_money + bet
                    leaving_money = leaving_money - bet
            
                if leaving_money <= 0:
                    print("You Busted! Leave the casino and go home.")

            print("Your Money Left: ", leaving_money)
            print()

        response = input ("Do you want to play another game: (yes/no)? ")
        if response == "no":
            continue_playing = "no"
            print("ThankYou For Playing At Our Casino.")
            print()
            print("You lost: $", lost_money)
            print("You Won: $", won_money)
            print("The amount you are leaving with: $", leaving_money)
            print()
            print("Please Come Back Again.")             
                          
dice_game()