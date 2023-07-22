
def game_start():
    """
    The function to start the game, with intro text.
    """
    #while game_intro = True:
    print("Hello, and welcome to the Crossroads where I, Crowley, is the crossroads demon. Are you here to make a deal?")
    deal_choice = input(">" )

    if deal_choice == "yes":
        print("Ok, please tell me what you want. Is it love, money or fame that you're after?")
        deal_choice = input("> ")
        if deal_choice == "love":
            print("Oh, you're after love I see. Your wish is granted!")
            print("You leave the crossroads and go back home. The day after, you're going out with your friend to a pub.")
            print("In the corner of the pub, you see a group of people, that you and your friend starts to talk to.")
            print("During the rest of the evening, two people out of the group have been flirting with you heavily during the night.")
            print("Their names are Harold and Anna, and both of them has asked you out for a date. Which one do you want to go out on a date with?")
            deal_choice = input("> ")
            if deal_choice == "Harold":
                print("You decided to go out with Harold. The date was a success, and he turned out to be your soulmate.")
            elif deal_choice == "Anna":
                print("You decided to go out with Anna. The date was a success, and she turned out to be your soulmate.")
            else:print("Invalid choice. Please select Harold or Anna")

        elif deal_choice == "money":
            print("You're a greedy bastard arent you.")
        elif deal_choice == "fame":
            print("You want the lifestyle of a famous one huh.")
        else: 
            print("Invalid choice. Please select love, money or fame.")

    elif deal_choice == "no":
        print("Thank you for playing. Goodbye")
    else:
        print("Invalid choice. Please select yes or no.")

game_start()