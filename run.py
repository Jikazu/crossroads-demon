import colorama
from colorama import Fore
colorama.init(autoreset=True)


def game_start():
    """
    The function to start the game, with intro text.
    """
    while True:
        print("You have stumbled upon a crossroads, where the legend says\n\
if you dig a hole in the dead center of the crossroads,\n\
and bury a box containing a picture of yourself, graveyard dirt\n\
and a bone from a black cat, a crossroads demon can be summoned.\n\
When making a deal with a demon they can make your dreams come true.\n\
You have all of these items, so you start digging and putting \n\
your items in the hole. After some 10 minutes have passed, you \n\
suddenly see a man appearing with glowing red eyes.")
        print(F'{Fore.RED}"Hello mortal, it is I, the crossroad demon\n\
Crowley. Tell me, who have summoned me here?"')
        tell_name()
        break

def tell_name():
    while True:
        name = input("> \n")
        if name != "":
            deal_time(name)
            break
        else:
            print("Please tell me your name.")


def deal_time(name):
    print(F'{Fore.RED}"Hello, ' + name + '.\n\
Are you here to strike a deal with me?')
    print(F'{Fore.RED}"The only thing I require from you to make your \n\
dreams come true, is a small payment, of your soul."')
    choice_one(name)
    print("Do you want to try again?")
    print("Options: Yes/No")
    while True:
        again = input("> \n")
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
        deal_choice = input("> \n")
        if deal_choice.lower() == "yes":
            print(F'{Fore.RED}"Please tell me what you want. Most of you \n\
humans either want one of two things. Love, or money."')
            choice_lovemoney()
            break
        elif deal_choice.lower() == "no":
            print("Why did you summon me then? Goodbye")
            break
        else:
            print("Invalid choice. Please select yes or no.")


def choice_lovemoney():
    """
    The function that brings you to the first dealchoice for love or money.
    """
    while True:
        print("Options: love/money")
        deal_choice = input("> \n")
        if deal_choice.lower() == "love":
            print("Oh, you're after love I see. Your wish of true love \n\
is granted and we have made a deal.\n\
You leave the crossroads and go back home. The day after, you're going \n\
out with your friend to a pub. In the corner of the pub, you see a \n\
group of people, that you and your friend starts to talk to.\n\
During the rest of the evening, two people out of the group \n\
have been flirting with you heavily during the night.\n\
Their names are Harold and Anna, and both of them has asked you out\n\
Which one do you want to go out on a date with?")
            love_choice()
            break
        elif deal_choice.lower() == "money":
            print("- You're a greedy bastard arent you. \n\
Money is the only thing on your mind isn't it.")
            print("You leave the crossroads and go back home. The day after,\n\
you decide to try your luck. You enter big mall. \n\
Do you want to buy a lottery ticket there from one of the kiosks?")
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
        deal_choice = input("> \n")
        if deal_choice.lower() == "harold":
            print("You decided to go out with Harold. The date was a success\n\
and he turned out to be your soulmate.")
            break
        elif deal_choice.lower() == "anna":
            print("You decided to go out with Anna. The date was a success,\n\
and she turned out to be your soulmate.")
            break
        else:
            print("Invalid choice. Please select Harold or Anna")


def money_choice():
    """
    The function that is called if you made the choice Money
    """
    while True:
        print("Options: yes/no")
        deal_choice = input("> \n")
        if deal_choice.lower() == "yes":
            print("You get a lottery ticket from one of the kiosks.\n\
The staff asks you if you want to get a euromillion or a lotto ticket.")
            print("Which one do you choose?")
            lottery_choice()
            break
        elif deal_choice.lower() == "no":
            print("You did not end up getting a lottery ticket. However, \n\
while in the mall, a talent scout from a big acting agency noticed you.\n\
She gave you her business card, and asked you to call her back to \n\
setup an audition. You called her back three days later. \n\
You smashed the audition, and you landed a supporting role in a small\n\
indie film, which turned out to be a big success.\n\
After that, producers wanted you in every project of theirs,\n\
and within two years, you were the star of a Marvel movie.\n\
You were swimming in money, and could barely spend more than you earned.\n\
The lifestyle of an actor though, started to take its toll.\n\
With all the partying you were doing, on one night four years\n\
after the big break, you decided to drive under the influence.\n\
You sadly got into a car crash, and passed away.\n\
Thus, Crowley came to collect your soul prematurely.")
            break
        else:
            print("Invalid choice. Please select yes or no.")


def lottery_choice():
    """
    The function that is called if you made the choice to buy a lottery ticket.
    """
    while True:
        print("Options: euromillion/lotto")
        deal_choice = input("> \n")
        if deal_choice.lower() == "euromillion":
            print("You decided to get a euromillion ticket, and went \n\
home after that to wait for the big day. Friday comes around,\n\
and eagerly you wait for the drawings. Turns out, you aced all\n\
the numbers with your ticket and won the jackpot of 400 million £.\n\
This will set you up for life so you decided to quit your job\n\
and started travelling the world.You ended up going on a trip\n\
of your lifetime, and visited all countries of the world in\n\
just shy of 9 years. You made so many friends during your trips,\n\
and with the endless amount of money you had, you donated money\n\
to local charities during your travels. After 10 years,\n\
on the day of the deal you made with Crowley, in the deep\n\
jungle of the Amazon, you suddenly see a face that you recognise.\n\
- Looks like you did not expect to see me here? It was\n\
Crowley, unfortunately.\n\
- It's time I collect my part of the deal,\n\
as I gave you everything you wanted.\n\
You sat down, when suddenly you felt a sharp pain in your chest, \n\
and slowly drifted off. The 10 year deal was up, and you didn't regret it.\n\
Crowley finally got his soul.")
            break
        elif deal_choice.lower() == "lotto":
            print("You ended up getting a lotto ticket, and went home\n\
to wait for the big day of the drawing. Turns out, you did win the \n\
jackpot of 100 million £. However, this was not enough for you. \n\
You had a friend who was slightly interested in crypto, that gave \n\
you advice, so once you got the money, you betted all the money\n\
you got in cryptocurrency. The one you invested in, increased by\n\
tenfold in size in just a few days, and you made quite a lot of money.\n\
You really did not want to pay all the taxes for this, so you opened\n\
up an offshore bank account in the Cayman islands where you transferred\n\
the money to. Turns out, tax evasion is quite the crime,\n\
and investigators found out what you had done. You tried to flee the\n\
country to go to Cayman islands, but they intercepted you. You ended\n\
up getting a 6 year prison scentence, and your life in prison,\n\
was not the best. You ended up bragging about all the money you got,\n\
and people got real tired of you, so one night you sadly got stabbed\n\
in your cell, and passed after just 6 months of making that deal.\n\
So, Crowley was quite pleased with the deal,\n\
and got to claim your soul much earlier than expected.")
            break
        else:
            print("Invalid choice. Please select yes or no.")


game_start()
