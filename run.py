def game_start():
    """
    The function to start the game, with intro text.
    """
    while True:
        print("You have stumbled upon a crossroads, where the legend says if you dig a hole in the dead center of the crossroads, and bury a box containing a picture")
        print("of yourself, graveyard dirt and a bone from a black cat, a crossroads demon can be summoned.")
        print("When making a deal with a demon, they can make your dreams come true.")
        print("You have all of these items, so you start digging and putting your items in the hole.")
        print("After some 10 minutes have passed, you suddenly see a man appearing with glowing red eyes.")
        print('"Hello mortal, it is I, the crossroads demon Crowley. Tell me, who have summoned me here?"')
        name = input("> ")
        print("Hello, " + name+ ". Ok, Are you here to strike a deal with me?" )
        print("The only thing I require from you to make your dreams come true, is a small payment, of your soul.")
        choice_one(name)
        print("Do you want to try again?")
        print("Options: Yes/No")
        while True: 
            again = input("> ")
            if again.lower() == "no":
                return
            elif again.lower() == "yes":
                break
            else: 
                print("Invalid choice. Please select yes or no")
        

def choice_one(name):
    """
    The function that brings you to select if you want to make a deal or not.
    """
    while True:
        print("Options: yes/no")
        deal_choice = input("> ")
        if deal_choice.lower() == "yes" :
            print("Please tell me what you want. Most of you humans either want one of two things. Love, or money.")
            choice_lovemoney()
            break
        elif deal_choice.lower() == "no":
            print("Thank you for playing. Goodbye")
            break
        else:
            print("Invalid choice. Please select yes or no.")

def choice_lovemoney():
    """
    The function that brings you to the first dealchoice for love or money.
    """
    while True:
        print("Options: love/money")
        deal_choice = input("> ")
        if deal_choice.lower() == "love":
            print("Oh, you're after love I see. Your wish of true love is granted and we have made a deal.")
            print("You leave the crossroads and go back home. The day after, you're going out with your friend to a pub.")
            print("In the corner of the pub, you see a group of people, that you and your friend starts to talk to.")
            print("During the rest of the evening, two people out of the group have been flirting with you heavily during the night.")
            print("Their names are Harold and Anna, and both of them has asked you out for a date. Which one do you want to go out on a date with?")
            love_choice()
            break
        elif deal_choice.lower() == "money":
            print("You're a greedy bastard arent you. Money is the only thing on your mind isn't it. ")
            print("You leave the crossroads and go back home. The day after, you decide to try your luck.")
            print("You enter big mall. Do you want to buy a lottery ticket there from one of the kiosks?")
            money_choice()
            break
        else: 
            print("Invalid choice. Please select love or money")

def love_choice():
    """
    The function that is called if you made the choice love
    """
    while True:
        print("Options: Harold/Anna")
        deal_choice = input("> ")
        if deal_choice.lower() == "harold":
            print("You decided to go out with Harold. The date was a success, and he turned out to be your soulmate.")
            break
        elif deal_choice.lower() == "anna":
            print("You decided to go out with Anna. The date was a success, and she turned out to be your soulmate.")
            break
        else:
            print("Invalid choice. Please select Harold or Anna")

def money_choice():
    """
    The function that is called if you made the choice Money
    """
    while True:
        print("Options: yes/no")
        deal_choice = input("> ")
        if deal_choice.lower() == "yes":
            print("You decided to get a lottery ticket. You decided to get a lottery ticket with random numbers, just for the heck of it.")
            lottery_choice()
            break
        elif deal_choice.lower() == "no":
            print("You did not end up getting a lottery ticket. However, while in the supermarket, a talent scout from a big acting agency noticed you.")
            print("She gave you her business card, and asked you to call her back to setup an audition. You called her back three days later.")
            print("You smashed the audition, and you landed a supporting role in a small indie film, which turned out to be a big success.")
            print("After that, producers wanted you in every project of theirs, and within two years, you were the star of a Marvel movie.")
            print("You were swimming in money, and could barely spend more than you earned. However, the lifestyle of an actor, started to take its toll.")
            print("With all the partying you were doing, on one night four years after the big break, you decided to drive under the influence.")
            print("You sadly got into a car crash, and passed away. Thus, Crowley came to collect your soul prematurely.")
            break
        else:
            print("Invalid choice. Please select yes or no.")


game_start()