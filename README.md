# Soup Playlist Bot
Create albums of music for other music bots which can then be ran with a single command.
# Install (Windows only, not tested on other platforms)
This bot requires Python 3.x and was tested on Python 3.5.2. [The Python download can be found here](https://www.python.org/downloads/)
1) Download or clone the bot
2) Run Install.bat
3) Follow instructions in command prompt

Providing that nothing went wrong the bot should be useable.

Note: This bot uses [Discord.py](https://github.com/Rapptz/discord.py), there are more in depth instructions should you have issues with installing libraries required for the bot.

**Warning: re-using the install script will overwrite both the albums and the settings files! Take care to not re-run them!**

# Using the bot
Run the bot using the Run.bat script. 

| Command          | Useage           |
| :-------------:  |:-------------:   |
|.create [Album name] | Creates an empty album |
| .summon        | summons the bot to the voice channel that the user is in |
| .add [Album name] [Song name/Link] |Adds a new song to an album |
|.play [Album name] |Plays the album |
|.random|Plays a random album|
|.shuffle [Album name]|Plays the album in a random order|
|.view [(Optional) Album name]| Views the album or all of the album titles|

The delay between messages sent is 2 seconds, because some music bots don't pick up the command if they're sent to quickly. Should you want to change the delay you must modify a variable then you must: open Src/Playlist.py in a test editor (e.g. VScode or Notepad++) and modify the follwing found at the top of the program.
```python
#Change the 2 to another value. The value must be in seconds. 
#You can have decimal values (e.g. 1.5 for one and a half seconds).
CommandDelay = 2
```
