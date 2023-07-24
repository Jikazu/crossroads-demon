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
            print("Oh, you're after love I see. Your wish is granted!")
            print("You leave the crossroads and go back home. The day after, you're going out with your friend to a pub.")
            print("In the corner of the pub, you see a group of people, that you and your friend starts to talk to.")
            print("During the rest of the evening, two people out of the group have been flirting with you heavily during the night.")
            print("Their names are Harold and Anna, and both of them has asked you out for a date. Which one do you want to go out on a date with?")
            love_choice()
            break
        elif deal_choice.lower() == "money":
            print("You're a greedy bastard arent you.")
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
            
game_start()