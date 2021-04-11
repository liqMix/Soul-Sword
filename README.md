# Soul Sword
My contribution to a community learning exercise for building a RogueLike game.
https://www.reddit.com/r/roguelikedev/

# Requirements
    tcod==12.2.0
    simpleaudio==1.0.4
    requests==2.25.1
    pillow==8.2.0
    pyYaml==5.4.1
	
# Description
I plan to use this project to explore multiple systems that I do not have much experience in.

# Current Features
 - Stochastic map generation from simple rules
 - Field of view
 - Entity seeding
 - Movement
 - Extremely basic AI pathing
 - Mugshot -> ASCII generation
 - Message box for communicating events
 
# Screenshots
## Title Screen
![Title Screen](https://liqmix.github.io/title-16a04199.jpg)
## In-Game
![In-Game with Enemy Selected](https://liqmix.github.io/game-62d6ddd3.jpg)
# Future Goals
 - Unique weapon upgrade system
	- All items (including corpses) have inherent stats
        - Your weapon has a number of slots these items can be put in to
	- Slotted items interact with adjacent items, either boosting or reducing certain stats
 - Procedurally generated randomized maps
	- Still looking for a unique source of noise to seed
 - Multiple element types - the usual suspects (fire, water, earth, ...)
 - Enemy type and strength sourced from public record inmate API
	- Arson -> fire type
	- DUI   -> water type
	- ...
 - HTML embedded as well as executable


# Disclaimer & Source
All information used to seed entities are available as public records. 
Out of respect for privacy, names are replaced and images are not stored.
The ASCII conversion of images are abstract representations with insufficient information for identification.

Any persons who do not consent to such use of their information as gathered from public records can contact me to be added to a blacklist.

## Clackamas County ##
Entities are sourced from the publicly available Clackamas County inmate roster API located here: https://web3.clackamas.us/roster/api/

All entities are presumed innocent until proven guilty in a court of law.

This project is not affiliated in any capacity with Clackamas County.

