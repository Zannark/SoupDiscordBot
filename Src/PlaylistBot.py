import discord
import asyncio
import json
import sys
import random

###

CommandDelay = 2

###

Client = discord.Client()
Data = None
UserName = ""
Password = ""
ChannelID = ""
PlayCommand = ""
DefaultTextChannel = ""
DefaultChannel = None

@Client.event
async def on_ready():
    C = Client.get_channel(ChannelID)
    await Client.join_voice_channel(C)

    DefaultChannel = Client.get_channel(DefaultTextChannel)
    await Client.send_message(DefaultChannel, "Bot is ready")

    print("Album bot is ready for use!")
    

@Client.event
async def on_message(message):
    DefaultChannel = Client.get_channel(DefaultTextChannel)

    Number = random.randint(1, 1000) 
    if Number == 5 or Number == 999:
        await Client.send_message(message.channel, "@here ayyyyyyyyy this is a number: " + str(Number))
    elif Number == 1:
        await Client.send_message(message.channel, "@everyone The number was 1.")

    Number = random.randint(1, 1000000)
    if Number == 69:
        await Client.send_message(message.channel, "@everyone Meme")
    
    if message.content.startswith('.summon'):
        C = Client.get_channel(ChannelID)

        for i in Client.voice_clients:        
            await i.move_to(message.author.voice.voice_channel)
    
    elif message.content.startswith('.add'):
        Command = message.content.split(' ')

        if len(Command) >= 3:
            try:
                Song = ""

                for i in range(2, len(Command)):
                    Song += (Command[i] + " ")
                
                Data[Command[1]].append(Song)

                with open("Data/Albums.json", mode="w") as JsonFile:
                    json.dump(Data, JsonFile)                           
            except:
                await Client.send_message(DefaultChannel, message.author.name + ", no album by the name of '" + Command[1] + "'")
        else:
            await Client.send_message(DefaultChannel, message.author.name + ", syntax is '.add <Album> <Link/Song name>'")

    elif message.content.startswith(".create"):
        Command = message.content.split(' ')

        if len(Command) == 2:
            if Command[1] in Data:
                await Client.send_message(DefaultChannel, Command[1] + " already exsists")
            else:
                Data[Command[1]] = []

            with open("Data/Albums.json", mode="w") as JsonFile:
                json.dump(Data, JsonFile)  
        else:
            await Client.send_message(DefaultChannel, message.author.name + ", syntax is '.create <Album name>'")

    elif message.content.startswith(".play"):
        Command = message.content.split(' ')

        if len(Command) == 2:
            if Command[1] in Data:
                for Element in Data[Command[1]]:
                    await Client.send_message(DefaultChannel, PlayCommand + " " + Element)
                    await asyncio.sleep(CommandDelay)
            else:
                await Client.send_message(DefaultChannel, Command[1] + " does not exsist") 
        else:
            await Client.send_message(DefaultChannel, message.author.name + ", syntax is '.play <Album name>'")

    elif message.content.startswith(".remove"):
        Command = message.content.split(' ')

        if len(Command) == 2:
            if Command[1] in Data:
                Data.pop(Command[1], None)

                with open("Data/Albums.json", mode="w") as JsonFile:
                    json.dump(Data, JsonFile)                
            else:
                await Client.send_message(DefaultChannel, Command[1] + " does not exsist")
        else:
            await Client.send_message(DefaultChannel, message.author.name + ", syntax is '.remove <Album name>'")

    elif message.content.startswith(".view"):
        Command = message.content.split(' ')

        if len(Command) == 2:
            if Command[1] in Data:
                await Client.send_message(DefaultChannel, "Songs in album " + Command[1]) 

                List = ""
                Counter = 1
                for Element in Data[Command[1]]:                    
                    List += str(Counter) + ". " + Element + "\n"
                    Counter += 1

                await Client.send_message(DefaultChannel, List)
            else:
                await Client.send_message(DefaultChannel, Command[1] + " does not exsist") 
        else:
            await Client.send_message(DefaultChannel, "Albums") 

            List = ""
            Counter = 1
            for Keys in Data:
                List += str(Counter) + ". " + Keys + "\n"
                Counter += 1

            await Client.send_message(DefaultChannel, List)

    elif message.content.startswith(".shuffle"):
        Command = message.content.split(' ')

        if len(Command) == 2:
            if Command[1] in Data:
                Shuffled = Data[Command[1]]
                random.shuffle(Shuffled)
                
                for Element in Shuffled:
                    await Client.send_message(DefaultChannel, PlayCommand + " " + Element)
                    await asyncio.sleep(CommandDelay)
            else:
                await Client.send_message(DefaultChannel, Command[1] + " does not exsist") 
        else:
            await Client.send_message(DefaultChannel, message.author.name + ", syntax is '.shuffle <Album name>'")

    elif message.content.startswith(".random"):
        Command = message.content.split(' ')

        Keys = list(Data.keys())
        Album = random.choice(Keys)

        for Element in Data[Album]:
            await Client.send_message(DefaultChannel, PlayCommand + " " + Element)
            await asyncio.sleep(CommandDelay)

    elif message.content.startswith(".help"):
        HelpMessage = "```\n"
        HelpMessage += "-----Start Help-----\n"
        HelpMessage += ".summon - summons the bot to the voice channel that the user is in\n"
        HelpMessage += ".create <Album name> - Creates a new empty album\n"
        HelpMessage += ".add <Album name> <Song name/Link> - Adds a new song to an album\n"
        HelpMessage += ".play <Album name> - Plays the album\n"
        HelpMessage += ".shuffle <Album name> - Plays the album in a random order\n"
        HelpMessage += ".random - Plays a random album\n"
        HelpMessage += ".view <(Optional) Album name> - Views the album or all of the album titles\n"
        HelpMessage += ".remove <Album name> - Deletes the album\n"
        HelpMessage += "-----End Help-----\n"
        HelpMessage += "```"
        
        await Client.send_message(DefaultChannel, HelpMessage)

with open("Data/Albums.json", mode="r") as JsonFile:
    Data = json.load(JsonFile)

with open("Data/Data.dat", mode="r") as AccountFile:
    Lines = AccountFile.readlines()
    if len(Lines) == 5:
        Username = Lines[0][0:-1]
        Password = Lines[1][0:-1]
        ChannelID = Lines[2][0:-1]
        PlayCommand = Lines[3][0:-1]
        DefaultTextChannel = Lines[4]
    else:
        print("Useage: Data/Data.dat -> \n<Email>\n<Password>\n<Default voice channel ID>\n<Play command>\n<Default text channel ID>")
        sys.exit(0)

Client.run(Username, Password)
