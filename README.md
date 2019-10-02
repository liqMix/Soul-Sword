# Soul Sword
My contribution to a community learning exercise for building a RogueLike game.
https://www.reddit.com/r/roguelikedev/

# Requirements
	tcod - https://pypi.org/project/tcod/
	requests - https://pypi.org/project/requests/
	numpy - https://pypi.org/project/numpy/
	Pillow - https://pypi.org/project/Pillow/2.2.1/
	simpleaudio - https://pypi.org/project/simpleaudio/
	
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
The ASCII conversion of images do not contain enough information to identify individuals.

Any persons who do not consent to such use of their information as gathered from public records can contact me to be added to a blacklist.

## Clackamas County ##
By not providing an API key, entities are sourced from the Clackamas County inmate roster API located here: https://web3.clackamas.us/roster/api/

This project is not affiliated in any capacity with Clackamas County.

## Jailbase API ## 
**Due to discrepancies between county records, this source is currently not supported, please run without providing a API key**
### API Access ###
An API key is required in order to access the full database. One can be acquired from https://rapidapi.com/jailbase/api/jailbase
The key should be placed in a text file:
<pre>data/key.txt</pre>
If the file does not exist, an alternative reduced-size keyless source will be used instead.

This project is not affiliated with JailBase.com.

Inmate data provided by JailBase.com
 
 Individuals are innocent until proven guilty in a court of law. 
 Data is believed to be reliable but is provided "as is". 
 Contact the appropriate governmental agency to verify.
 
Terms of Service:
 https://www.jailbase.com/api/terms/
