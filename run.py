
def game_start():
    """
    The function to start the game, with intro text.
    """
    #while game_intro = True:
    print("Hello, and welcome to the Crossroads where I, Crowley, is the crossroads demon. Are you here to make a deal?")
    deal_choice = input(">" )

    if deal_choice == "yes":
        print("Ok, please tell me what you want.")
    elif deal_choice == "no":
        print("Thank you for playing. Goodbye")
        restart()
    else:
        print("Invalid choice. Please select yes or no.")

game_start()