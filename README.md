# discord-voice-notifier
A simple Discord bot that notifies you when people join voice channels

## Goal
This is a simple Discord bot, written in Python. It listens for people joining voice channels on a server, and then posts their name to a specified text channel. This means you get get push notifications for when people join voice channels, which is something that Discord currently doesn't provide.

## Setup
You can set this bot up very simply on a GCP Compute Engine e2-micro instance, which is [free]([url](https://cloud.google.com/free/docs/free-cloud-features#compute)). Create your VM, then ssh into it and run the following:
```
sudo apt update
sudo apt install python3-pip
sudo apt install python3.11-venv
```
You can then create a virtual environment and install the discord.py library:
```
python3 -m venv ~/discord_bot
~/discord_bot/bin/pip3 install discord.py
```
Then we can create the bot.py file, open it with nano, and paste in the bot.py code from this repository. You can also do this by cloning the repo etc, but these instructions are aiming to be as simple as possible.

```
cd discord_bot
touch bot.py
nano bot.py
```
You should replace the channel and token variables. For channel, you can right-click the text channel you want the bot to post in, and click 'Copy link'. The number at the end of the link is the channel ID. For the token, you will get a token when you [set up your Discord bot]([url](https://discordpy.readthedocs.io/en/stable/discord.html)). You can just paste it in here, but best practice is to use something like [dotenv]([url](https://pypi.org/project/python-dotenv/)) to make sure you don't leak your secret information.

Once you have bot.py ready, you can run it:
```
~/discord_bot/bin/python3 bot.py
```

Your bot is now running. You can use the Discord developer UI to get a link to add your bot to your server, and you're good to go! Now when someone joins a voice channel, your bot will post a message containing their name to the channel you specified. You can set up notifications for yourself from that text channel, and now you have push notifications when your friends join voice channels!
