<div>
    <h1 align="center"> Loham[FastAPI] </h1>
</div>

<div style="text-align: left;">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" width="150" style="border-radius: 10rem;">
</div>



---
## About
<p>This is an api built on top of fastAPI and Uvicorn server and jwt for authentication and authorization. your probably gonna ask why FastAPI uses Uvicorn by default Uvicorn is an ASGI server, which means it communicates using the Asynchronous Server Gateway Interface, a modern standard for Python asynchronous applications. </p>
---


## Project Overview

A C++ SFML Simple Snake game with custom game engine [Snake](https://github.com/abdimk/Snake) .



## Features

-   🌙 
-   🧰 Collusion detection 
-   📚 custome state and texture
-   🏡 Customizable layout
-   ✏️ Optional built-in library for manipulating SFML 

## Non-goals
....

## Where do I start?

Head over to the [installation](https://lune.gitbook.io/lune/home/installation) page to get started using Lune!


```
pip3 install -r requirments.txt
```
-------
  
<div align="center">
<h1><img src="https://telegra.ph/file/c182d98c9d2bc0295bc86.png" width="45"><b>  
DirectoryLayout <b></h1>
</div>


```

├── .gitignore                          
├── LICENSE
├── README.md
├──
├── requirements.txt                   ( For keeping all the library name wich project is using)
├── app
│   │
│   ├── __init__.py                   ( Initializing the bot from here.)
│   ├── companies.db                  ( Importing and storing all envireonment variables from config.env)
│   ├── main.py
|   |                  ( Help in logging and get log file)
│   ├── company                        ( An assets folder to keep all type of assets like thumbnail, font, constants, etc.)
│   │   └── __init__.py
|   |   |── database.py
|   |   |── models.py
|   |   |── oauth2.py
|   |   |── schemas.py
|   |   |── token.py
│   │   └─── routes
│   │          └── __init__.py
|   |          |── auth.py
|   |          └── comp.py
|   |          └── users.py
|___|                            

```
  
-------
  
<div align="center">
<h1><b>Basic structure for building your own plugin.</b></h1>
</div>


```py
from TelegramBot.helpers.decorators import ratelimiter
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["hello", "hi"]))
@ratelimiter
async def hello(client: Client, message: Message):
    """
    simple plugin to demonstrate in readme.
    """   	
    return await message.reply_text("world")	    
```
	    
_____
  
<div align="center">
<h1><b>Credits and Contibution</b></h1>
</div>
  
<img src="https://telegra.ph/file/b26313d73e4d05de84a85.png" align="right" width="150">
<p>
Codes and structure of this bot is heavily inspired by open source projects like <a href="https://github.com/TeamYukki/YukkiMusicBot"><strong>YukkiMusicbot</strong></a> | <a href="https://github.com/UsergeTeam/Userge"><strong>Userge</strong></a> | <a href="https://github.com/EverythingSuckz/TG-FileStreamBot"><strong>TG-FileStreamBot etc.</strong></a>.
<br>
<br>
 Special Thanks to <br>
• <a href="https://github.com/delivrance"><strong>Dan</strong></a> for creating <a href="https://github.com/pyrogram/pyrogram"><strong>Pyrogram.</strong></a><br>
• <a href="https://github.com/starry69"> Starry</a> for guiding and acutebot repository. <br>
• <a href="https://github.com/annihilatorrrr">Annihilator</a> for helping me out with pyrogram stuff.

<br>
<br>
Any type of suggestions, pointing out bug or contribution is highly appreciated. :)
</p>
 
