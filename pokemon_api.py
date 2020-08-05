import requests
import pprint

# user can input what pokemon they want to look up
poke = input("What Pokemon do you wish to learn about? ")

# insert that pokemon into url to fetch from pokeapi.co
poke_api = f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}/"

poke_json = requests.get(poke_api)  # is a json object

poke_json = poke_json.json()

print(poke_json)