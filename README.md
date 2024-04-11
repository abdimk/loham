<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->

<div align="center">
	<h1> Loham 🐍 </h1>
	<div>
		<a href="">
			<img src="https://img.shields.io/crates/v/lune.svg?label=Version" alt="Current Lune library version" />
		</a>
		<a href="">
			<img src="https://shields.io/endpoint?url=https://badges.readysetplay.io/workflow/filiptibell/lune/ci.yaml" alt="CI status" />
		</a>
		<a href="">
			<img src="https://shields.io/endpoint?url=https://badges.readysetplay.io/workflow/filiptibell/lune/release.yaml" alt="Release status" />
		</a>
		<a href="">
			<img src="https://img.shields.io/github/license/filiptibell/lune.svg?label=License&color=informational" alt="Current Lune library version" />
		</a>
	</div>
</div>

---
## about
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




-------
  
<div align="center">
<h1><img src="https://telegra.ph/file/c182d98c9d2bc0295bc86.png" width="45"><b>  
DirectoryLayout <b></h1>
</div>


```

├── Dockerfile                          
├── LICENSE
├── README.md
├── config.env                         ( For storing all the  environment variables)
├── requirements.txt                   ( For keeping all the library name wich project is using)
├── TelegramBot
│   │
│   ├── __init__.py                   ( Initializing the bot from here.)
│   ├── __main__.py                   ( Starting the bot from here.)
│   ├── config.py                     ( Importing and storing all envireonment variables from config.env)
│   ├── logging.py                    ( Help in logging and get log file)
│   │
│   ├── assets                        ( An assets folder to keep all type of assets like thumbnail, font, constants, etc.)
│   │   └── __init__.py
│   │   ├── font.ttf
│   │   └── template.png
│   │
│   ├── database                      (Sperate folder to manage database related stuff for bigger projects.)
│   │   ├── __init__.py
│   │   ├── database.py              (contain functions related to handle database operations all over the bor)
│   │   └── MongoDb.py               (Contain a MongoDB class to handle CRUD operations on MongoDB collection )
│   │  
│   ├── helpers                       ( Contain all the file wich is imported and  used all over the code. It act as backbone of code.)
│   │   ├── __init__.py
│   │   ├── filters.py 
│   │   ├── decorators.py            ( Contain all the python decorators)
│   │   ├── ratelimiter.py           (Contain RateLimiter class that handle ratelimiting part of the bot.)
│   │   └── functions.py             ( Contain all the functions wich is used all over the code. )
│   │
│   ├── plugins                       ( plugins folder contain all the plugins commands via wich user interact)  
│   │   ├── __init__.py 
│   │   ├── developer
│   │   │   ├── __init__.py
│   │   │   ├── terminal.py
│   │   │   └── updater.py
│   │   │
│   │   ├── sudo
│   │   │   ├── __init__.py
│   │   │   ├── speedtest.py
│   │   │   ├── dbstats.py
│   │   │   └── serverstats.py
│   │   │   
│   │   └── users
│   │       ├── __init__.py
│   │       ├── alive.py
│   │       └── start.py
│   │      
│   └── version.py         
└── start                             ( A start file containing bash script to start the bot using bash start)

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
 
