# CROSSROADS


## INDEX

+ [Introduction](#Introduction "Introduction")
   + [Links](#Links "Links")
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

[Live link for game](https://crossroads-demon-ee600f84f79d.herokuapp.com/)
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

![flowchart](/images/flochart.jpg)

All the stories lead to certain death, but some stories are nicer than others. It's not a very happy game, but then again,  life is not always happy either.
For each choice in the story there is a print of what choices can be made. 


## Features

1. Users are greeted with an introtext and it gets right into the story, explaining how to summon a demon. It sets the scene and fans of the Supernatural show
will immediately know what is being summoned, and who. It also asks for the name of the person who did the summoning.

![game start](/images/gamestart.png)

2. The name cannot be empty as that will give you


### Existing features

## Technologies used

- Python [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Testing
Test of functionality and appearance of the website has have been dealt with troughout the development process. 
Tests has been conducted with Google Chrome on different devices.

I've listed my main issues here - 


Other than the above, I had some validation errors in my code with lines that were too long, with random blankspaces, not enough lines in between etc.



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

Create an account or log-in to Heroku on www.heroku.com
There are now extra requirements for security, so you will need a 2fa authenticator app.
Press the button where it says you can create a new app.
Go to 'settings'. Even if you do not have an API to link with the app,
Now, on the same page, there's the option to add buildpacks. These need to be built in this specific order: first of all, Python (press save), then Node.js (press save). Python should appear above Node.js on the list of added buildpacks.
Now, go to the 'deploy' page.
Link your project via Github, here, and choose the right repo.
Click on 'enable automatic deployment'
You may need to make a change in GitPod and commit & push it after this process in order to trigger automatic deployment.
Press the 'open app' button and you should see your app. You can get your deployed link here, or it should be in green on the deply page after a few minutes.
   

## Content

- All content on this site has been produced by the author of this project. 



## Credits

Many thanks to:

Martina Terlevic
 - My mentor

 Slack.

 ### Great webpages

 Sites that I've used a lot during this project to look up various things are:

 https://www.w3schools.com/
 https://www.youtube.com


 And all the previous lessons in Python Essentials and the Walkthrough project ”Love Sandwiches!”.

Kind Regards,
Gabriella