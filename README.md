# Soul Sword (tentative)
My contribution to a community learning exercise for building a RogueLike game.
https://www.reddit.com/r/roguelikedev/

# Requirements
	tcod - https://pypi.org/project/tcod/
	
# Description
I plan to use this project to explore multiple systems that I do not have much experience in.

# Goals/Features
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

# API Access
An API key is required in order to access the full database. One can be acquired from https://rapidapi.com/jailbase/api/jailbase
The key should be placed in a text file:
<pre>data/key.txt</pre>
If the file does not exist, an alternative reduced-size keyless source will be used instead.

# Disclaimer
Current implementation does not replace or obfuscate names sourced from JailBase.com. This may change in the future.

This project is not affiliated with JailBase.com.
Any persons who do not consent to such use of their information as gathered from public records can contact me to be added to a blacklist.

Inmate data provided by JailBase.com
 
 Individuals are innocent until proven guilty in a court of law. 
 Data is believed to be reliable but is provided "as is". 
 Contact the appropriate governmental agency to verify.
 
Terms of Service:
 https://www.jailbase.com/api/terms/
