from ollama import chat
import asyncio
import json
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
import httpx


load_dotenv()
api_data = {

    "client_id": "c260f00d-1071-409a-992f-dda2e5498536",

    "grant_type": "api_token",

    "scope": "app:realm-api app:pricing-api",

    "token": os.getenv("TOKEN")

}
get_api_token = httpx.post("https://auth.tradeskillmaster.com/oauth2/token",data=api_data)
token = get_api_token.json()['access_token']
headers = {
    "Authorization": f'Bearer {token}'
}

region_id = "2" # europe region
realm_id = "511" #burning legion realm
auction_house_id = "175" #burning legion auction house id


realms = "https://realm-api.tradeskillmaster.com/realms"

all_for_region= f'https://pricing-api.tradeskillmaster.com/region/{region_id}'

user_input = input("For what mount currently on AH are you interested in? \n")
user_input = user_input.lower()

#opening file
with open("mounts.json") as file: 
#load list of json objects
  mounts_data = json.load(file)
  for mount in mounts_data:
#look for mount in file
    if user_input == mount['name']:
      print("Found it")
      item_id = mount['id']

#get AH info about specified mount
get = f'https://pricing-api.tradeskillmaster.com/ah/{auction_house_id}/item/{item_id}' 

get_item_info = httpx.get(url=get, headers=headers)

item_summary = json.loads(get_item_info.content)

data =[ {
      "role": "system",
      "content": """   You are an WoW auction house expert. You are analysing json data you get from users TSM get api call response.
                give him the basics like an item name, current marketvalue, historical price, minimum buyout and number of active auctions.
                Only return the suggested information.
                Base your answer only on data send to you by the user.
                You are analyzing World of Warcraft auction house data.
                Convert all prices into the following human-readable format:
                Use full units: g for gold, s for silver
                Format the gold value with commas (e.g. 52,599g)
                Do not include copper, always show with gold only
                1 gold = 10000 copper, dont use dolars only gold
                keep in mind that max value is 999.999.999
                keep your answer really short

                """
    },
    {
        "role": "user",
        "content": f"Analyze this item price data in copper about {user_input}: {item_summary}"
    }
]
#send user and system prompt to local model
response = chat('llama3.2',messages=data,think=False)

table = Table(title="Mounts on WoW Auction House")
table.add_column("Mount name",style="red",no_wrap=True,justify="center",vertical="middle")
table.add_column("Market Information",style="cyan",no_wrap=False,justify="center")
table.add_row(f'{user_input}',f'{response.message.content}')
console = Console()
console.print(table)


