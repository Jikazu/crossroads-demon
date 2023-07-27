# CROSSROADS


## INDEX

+ [Introduction](#introduction "Introduction")
   + [Links](#links "Links")
+ [UX](#ux "UX")
   + [Site Purpose](#site-purpose "Site Purpose")
+ [Design](#design "Design")
+ [Logic and Structure](#logic-and-structure "Logic and Structure")
+ [Features](#features "Features")
+ [Technologies Used](#technologies-used "Technologies used")
+ [Testing](#testing "Testing")
   + [Validator Testing](#validator-testing "Validator Testing")
   + [Unfixed bugs](#unfixed-bugs "Unfixed bugs")
+ [Development and Deployment](#development-and-deployment "Development and Deployment")
+ [Content](#content "Content")
+ [Credits](#credits "Credits")
+ [Great Webpages](#great-webpages "Great webpages")

# Introduction

This little text&choice based game is inspired by the show [Supernatural](https://en.wikipedia.org/wiki/Supernatural_(American_TV_series)) created by Eric Kripke.
It follows two brothers, Sam and Dean Winchester as they hunt demons, ghosts and other supernatural beings. In one of the episodes they meet a crossroads demon called Crowley.
When I was brainstorming ideas for this, as I wanted it to be a a choice based game, that character popped up in my head as it would translate well into a text based game to explore
how ones choices can affect the outcome of ones life. 

However, none of the choices end up well, since in the show if you make a deal with a demon, you'll only live for 10 years until they come to collect their payment, which is your soul.
This plays with the idea that if you try to take shortcuts in life, the outcome might not be the best.

It starts with a short introduction of the premise of how to summon one of these demons, which you do, and he asks you for your name.

![Game intro screen](/images/gamestart.png)

Above is a screenshot of the start of the game.

## Links

[Live link for the game](https://crossroads-demon-ee600f84f79d.herokuapp.com/)<br>
[Link to the GitHub repo](https://github.com/Jikazu/crossroads-demon)


# UX

### Site Purpose:
This game is created for my third project in Code Institute's fullstack course, which is to create a simple game app using python.
Users can interact with the game, and it's replayable to some degree as the choices have different outcomes.

### As a first time user:

* I wanted the game start with a little introduction of how one can summon a crossroads demon to make a deal with, as they describe it from the show.
* I want users to enjoy the process and get a sense of curiosity of what will happen when you make a choice.
* I want people to get shocked at the end, as we all will die sooner or later.

### For returning users:

* I wanted to give returning users alternative choices that you might not choose the first time you play through it.


## Design
This is my first project made completely in python, and as the command line is quite limited, I wanted to atleast add some colour to the text.
I've added a red colour to Crowley's dialouge as he is a demon with red eyes, so it felt fitting. I used the Colorama library to achieve that. 

![crowleydialouge](/images/crowleytext.png)

I tested around with adding colour to the rest of the text aswell, but as it's a story with quite a lot of text at some parts. The default
white colour is a quite good one to use already as another colour such as blue might be more difficult to read. I also had the 79 character
limit to adhere to per row, and adding colour to some lines would make the block of text look odd at times.

I did add some green text at the very end where I thank you for playing my game. 

![end of game](/images/thankyou.png)

## Logic and structure

Below is a hand-drawn flowchart showing the paths that you can take throughout the game and how it ties together. 

![flowchart](/images/flowchart.jpg)

All the stories lead to certain death, but some stories are nicer than others. It's not a very happy game, but then again,  life is not always happy either.
For each choice in the story there is a print of what choices can be made. 


## Features

1. Users are greeted with an introtext and it gets right into the story, explaining how to summon a demon. It sets the scene and fans of the Supernatural show
will immediately know what is being summoned, and who. It also asks for the name of the person who did the summoning.

![game start](/images/gamestart.png)

2. The name cannot be empty as that will give you a message from Crowley to please tell him your name.

![name](/images/tellname.png)

It is only the name that has a free option, as all the other stages you get presented with two options. 
If you select yes out of the two options, you will get further in the story, as its my equivalent of "do you want to play the game".
If you say no, Crowley will get mad at you and go away. You will get prompted again if you want to play again. If you say no there, the game ends.

![options](/images/options.png)
![dont want to play](/images/noplay.png)

It is not case sensitive, as I'm using a .lower() function in my code. 
If you however make a typo, or write something completely else or just press enter it will prompt you again for a correct input.

![invalidchoice](/images/invalidchoice.png)

There are two main ways that the story can go, either for love or money. As I mentioned previously in my readme, all the stories will end in death,
and will loop back to do you want to play again. All the stories are different however based on your choices along the way.

Below is one example of an ending if we go down the money choices. 

![money ending](/images/moneyending.png)

### Future features

+ It would be nice to go deeper with the story, and add a renegotiation with Crowley for 10 more years.
+ Could be fun to add a section where you can choose to try and kill Crowley so you can continue living your life instead of dying after 10 years.

## Technologies used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Colorama](https://pypi.org/project/colorama/)

## Testing
Test of functionality and appearance of the app has have been dealt with troughout the development process. 
Tests has been conducted with Google Chrome on different devices.

I've listed my main issues here - 

1. Could press enter to skip by entering the name.
    - Solution: Added an if set for the name, if the string is not empty to go to the next function, and if it's empty to loop back to enter the name.
2. I firstly tried to put everything in one big function, but then if you put in a wrong input it would loop back all the way to the beginning.
    - Solution: Broke down each choice to its own function with its own loop and called each function if the choice was correct such as yes/love/money etc. Also added breaks to break out of loops.
3. Code did not pass the validation as my lines were too long, and I didn't know how to break up the print statements so it would pass.
    - Solution: For it to look nicer and pass, I put all the print statements into bigger statements and used the \n\ to split them into different rows instead different prints.

Other than the above, I had quite a lot of validation errors in my code with lines that were too long, with random blankspaces, not enough lines in between etc.
I've also confirmed that each choice goes to where it's supposed to be, all inputs need to be correctly inputted without any blank enters, and that the loops break where they should so the options to play again will come up at the end.

### Validator Testing

-HTML
- No errors were returned when running it through the Code Institute [Python linter](https://pep8ci.herokuapp.com/)

![python validator](/images/pythonvalidator.png)

   
### Unfixed Bugs

None that I am aware of.

All other known bugs are in the [Testing](#testing) section, with their solution. 

## Development and Deployment

The development environment used for this project was GitPod. To track the development stage and handle version control I've done regular commits and pushes sto GitHub. The GitPod environment was created by using a template provided by Code Institute. 

The live version of the project is deployed at Heroku.

The stages are as follows:

Create an account or log-in to Heroku on www.heroku.com<br>
There are now extra requirements for security, so you will need a 2fa authenticator app.<br>
Press the button where it says you can create a new app.<br>
Go to 'settings', as there's the option to add buildpacks.<br>
These need to be built in this specific order: first of all, Python (press save), then Node.js (press save). Python should appear above Node.js on the list of added buildpacks.<br>
Now, go to the 'deploy' page.<br>
Link your project via Github, here, and choose the right repo.<br>
Click on 'enable automatic deployment'<br>
You may need to make a change in GitPod and commit & push it after this process in order to trigger automatic deployment.<br>
Press the 'open app' button and you should see your app. You can get your deployed link here, or it should be in green on the deply page after a few minutes.<br>
   

## Content

- The story is inspired by the character Crowley in the show Supernatural, but the stories and text in this game is created by the author of this project. 



## Credits

Many thanks to:

Martina Terlevic
 - My mentor

 Slack.

 ### Great webpages

 Sites that I've used a lot during this project to look up various things are:

 https://www.w3schools.com/<br>
 https://www.youtube.com


 And all the previous lessons in Python Essentials and the Walkthrough project ”Love Sandwiches!”.

Kind Regards,
Gabriella