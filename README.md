<div>
    <h1 align="center"> Loham[FastAPI] </h1>
</div>

<div style="text-align: left; border-radius: 10px;">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" width="150">
</div>





---
## About
<p>This is an api built on top of fastAPI and Uvicorn server and jwt for authentication and authorization. your probably gonna ask why FastAPI uses Uvicorn by default Uvicorn is an ASGI server, which means it communicates using the Asynchronous Server Gateway Interface, a modern standard for Python asynchronous applications. </p>
---

  
<div align="center">
<h2></h1><img src="https://telegra.ph/file/c182d98c9d2bc0295bc86.png" width="20"><b>  
DirectoryLayout<b></h1>
</div>


```

├── .gitignore                     (to preventing unnecessary files from being tracked)           
├── LICENSE                        (for specifying the terms under which the code can be used, modified, and distributed)
├── README.md                      (a github file repository is crucial for providing essential information about your project)
├──
├── requirements.txt               ( For keeping all the library name wich project is using)
├── app
│   │
│   ├── __init__.py                 ( Initializing the package from here.)
│   ├── companies.db                (A SQLite database file for storing all information related to companies)
│   ├── main.py			    (The main Python script for running the application)
|   |                  
│   ├── company                     (A directory containing code related to company management)
│   │   └── __init__.py
|   |   |── database.py  	    (Python code for interacting with the SQLite database)
|   |   |── models.py               (Python code defining data models for companies)
|   |   |── oauth2.py  		    (Python code for OAuth2 authentication)
|   |   |── schemas.py              (Python code defining Pydantic schemas for data validation)
|   |   |── token.py                (Python code for generating authentication tokens)
│   │   └─── routes                 (A directory containing API routes for company-related operations)
│   │          └── __init__.py   
|   |          |── auth.py          (Python code defining authentication routes)
|   |          └── comp.py          (Python code defining CRUD operations for companies)
|   |          └── users.py         (Python code defining CRUD operations for users)
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



## Installation 
<p>First start by installing the requirments by doing</p>

```
pip / pip3 install -r requirments.txt [windows / mac os | linux]
```
-------
  
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
 
