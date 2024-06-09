<div>
    <h1 align="center"> Loham</h1>
</div>

<p align="center"><em>Highly Organized Business Directory API</em></p>
<p align="center"> 41k filtered records out of 100k</p>

<div align="center">
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" width="150"></a>
    <a href="https://fastapi.tiangolo.com/"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="150"></a>
    <a href="https://jwt.io/"><img src="https://seeklogo.com/images/J/jwt-logo-11B708E375-seeklogo.com.png" width="150"></a>
    <a href="https://www.uvicorn.org/"><img src="https://img.stackshare.io/service/12834/uvicorn.png" width="100"></a>
</div>


<div>
    <br>
    <br>
    <br>
    <br>
</div>

<p align="center" dir="auto">
<a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster">
    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&amp;branch=master" alt="Test" style="max-width: 100%;">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/fastapi" rel="nofollow">
    <img src="https://camo.githubusercontent.com/f63da5c04568c26cac1b9a03c24ed3843ce6602ba795bd3d4afea2641d7d1ca6/68747470733a2f2f636f7665726167652d62616467652e73616d75656c636f6c76696e2e776f726b6572732e6465762f7469616e676f6c6f2f666173746170692e737667" alt="Coverage" data-canonical-src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg" style="max-width: 100%;">
</a>
    
<a href="https://pypi.org/project/fastapi" rel="nofollow">
    <img src="https://camo.githubusercontent.com/97779323fa03e0a4ec57beb1ba34c1038a2974842e06e6ba4c899f4226b84370/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f666173746170692e7376673f636f6c6f723d253233333444303538" alt="Supported Python versions" data-canonical-src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" style="max-width: 100%;">
</a>
</p>



---
## About
<p>Business Directory API built on top of <strong>FastAPI</strong> and <strong>Uvicorn Server</strong> uses JWT for authentication and authorization. FastAPI has native support for Uvicorn,Uvicorn is an ASGI server, which means it communicates using the Asynchronous Server Gateway Interface, a modern standard for Python asynchronous applications. </p>


  
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
<h1><b>Basic structure </b></h1>
</div>


## To see the version 
```py
import requests
import json

req = requests.get('https://loham.onrender.com/v1/about')
data_str = req.content.decode('utf-8')
json_data = json.loads(data_str)

print(json.dumps(json_data, indent=4))	    
```

```curl
curl -X 'GET' \
  'https://loham.onrender.com/v1/about' \
  -H 'accept: application/json'
```

### output
```json
{
    "Version": "0.0.1",
    "Developer": "Abdisa (Netkas) | (0_0)",
    "Released Year": "April 10 2024",
    "Github": "https://github.com/abdimk/loham"
}

```
## Get category count 
```py
import requests
import json

req = requests.get('https://loham.onrender.com/get_category_count')
data_str = req.content.decode('utf-8')
json_data = json.loads(data_str)

print(json.dumps(json_data, indent=4))
```

## output
```json
    [
{
        "categories": "Foreign Suppliers to Ethiopia",
        "category_count": 49
    },
    {
        "categories": "Hotels and Restaurants, Tour and Travel",
        "category_count": 64
    },
    {
        "categories": "Insurance Brokerage",
        "category_count": 18
    },
    {
        "categories": "Micro and Small Enterprises in Ethiopia",
        "category_count": 3931
    }
]
```

## Get Company with db id
```py
import requests
import json

id = 609
req = requests.get(f'https://loham.onrender.com/get/{id}')
data_str = req.content.decode('utf-8')
json_data = json.loads(data_str)

print(json.dumps(json_data, indent=4))
```
## output

<p>The output is based of the specified schema in fastAPI(response schema)</p>

```json
{
    "id": 609,
    "company_name": "CAROGA PHARMA ETHIOPIA PLC",
    "phone_number": "+25 11 4161090/4165159/4654944",
    "mobile": "+251 91 1209007",
    "fax": "+251 11 4654595",
    "sub_city": "Kirkos",
    "business_type": "Private",
    "location": "Addis Ababa, Ethiopia",
    "url": "https://www.2merkato.com/directory/709-caroga-pharma-ethiopia-plc",
    "primary_category": "None",
    "categories": "Commission Agent"
}

```

### Get companies with initals in thier name

```py
import requests
import json


#common key initals are like agro,pharma,agents,consultancy,export,import

key = 'export'  # for example to get companies that have pharma in their name
req = requests.get(f"https://loham.onrender.com/get_with_initals/{key}")
data_str = req.content.decode('utf-8')
json_data = json.loads(data_str)

print(json.dumps(json_data, indent=4))
```

### output


```json
returns a list of arryays max 10 for free users


[
    {
        "id": 57,
        "company_name": "GIGAR TRADING IMPORT, EXPORT & DISTRIBUTOR",
        "phone_number": "+251 11 5518267/5505853/54",
        "mobile": "+251 91 1201117",
        "fax": "+251 11 5502911",
        "sub_city": "",
        "business_type": "Private",
        "location": "Addis Ababa",
        "url": "https://www.2merkato.com/directory/11267-gigar-trading-import-export-distributor",
        "primary_category": "None",
        "categories": "Commercial Agent"
    },
    {
        "id": 68,
        "company_name": "Tsegaab Teklu Import Export PLC",
        "phone_number": "+251-11-6525213",
        "mobile": "",
        "fax": "",
        "sub_city": "Kirkos",
        "business_type": "",
        "location": "Tsegaab Teklu Import Export PLC: Import and Export. Kirkos Sub-City Addis Ababa Region 14 15963 City: Addis Ababa Administrative region: Addis Ababa Country: Ethiopia, Addis Ababa, Ethiopia",
        "url": "https://www.2merkato.com/directory/16504-tsegaab-teklu-import-export-plc",
        "primary_category": "None",
        "categories": "Commercial Agent"
    }
]
```

### Get with initals with post request

```py
import requests
import json


url = 'https://loham.onrender.com/get_with_initals'

# payload = {
#     "company_name": "string", # Optional
#     "sub_city": "string", #Optional
#     "business_type": "string",  #Optional
#     "primary_category": "string", #Optional
#     "categories": "string" #Optional
#   }

payload = {
    "sub_city": "yeka",
    "business_type": "private",
    "categories": "Ethiopian Importers"
    }

req = requests.post(url, json=payload)
data_str = req.content.decode('utf')
json_data = json.loads(data_str)

print(json.dumps(json_data, indent=4))
```
### output

<p> list of arrays max 10 results</p>



```json
[
    {
        "id": 3511,
        "company_name": "Sisay Gulema Building Material General Importer",
        "phone_number": "+251 115 15 58 11",
        "mobile": "+251 911 21 21 16",
        "fax": "+251 115 15 21 24",
        "sub_city": "yeka",
        "business_type": "Private",
        "location": "Urael, Besides Ministry of Agriculture and Urban Development, Addis Ababa, Ethiopia",
        "url": "https://www.2merkato.com/directory/14864-sisay-gulema-building-material-general-importer",
        "primary_category": "Pipes and Fittings/polypopylene",
        "categories": "Ethiopian Importers"
    },
    {
        "id": 3540,
        "company_name": "Dagem Kennedy General Trading PLC",
        "phone_number": "",
        "mobile": "+251 930 11 03 26, +251 911 62 67 84, +251 930 11 03 25",
        "fax": "",
        "sub_city": "Yeka",
        "business_type": "Private",
        "location": "22 Mazoria, Behind H&M Building, House #1006, Addis Ababa, Ethiopia",
        "url": "https://www.2merkato.com/directory/19748-dagem-kennedy-general-trading-plc",
        "primary_category": "Electrical Materials/Equipments",
        "categories": "Ethiopian Importers"
    }
]
```



### Get(search) with phone number 
```py
import requests
import json

url = 'https://loham.onrender.com/get_with_phone'

payload = {
    "phone_number": "251116",
    "limit": 10 # the no of results you want to get
    }

req = requests.post(url, json=payload)
data_str = req.content.decode('utf')
json_data = json.loads(data_str)

print(json.dumps(json_data, indent=4))
```

<p> returns an array of list companies type</p>
_____


<!--
## Installation 
<p>First start by installing the requirments by doing</p>

```
pip / pip3 install -r requirments.txt [windows / mac os | linux]
```
-------
    -->
<div align="center">
<h1><b>Credits and Contibution</b></h1>
</div>


<!-- <p>
Codes and structure of this bot is heavily inspired by open source projects like <a href="https:/"><strong></strong></a> | <a href=""><strong>Userge</strong></a> | <a href=""><strong>TG-FileStreamBot etc.</strong></a>. -->
<br>
 Special Thanks to 
 <br>
 <br>
• <a href="https://github.com/tiangolo">Tiangolo</strong></a> for creating <a href="https://github.com/tiangolo/fastapi"><strong>FastAPI</strong></a><br>
<!-- • <a href=""></a> <br>
• <a href=""></a> -->

<br>
<br>

<img src="https://pbs.twimg.com/media/CsjbGV6W8AAvBWi.jpg" width="150">
<p>Any type of suggestions, pointing out bug or contribution is highly appreciated :).</p>
 
