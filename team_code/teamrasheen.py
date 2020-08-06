import requests
import wget
import json

def main():
    wget_pic(api_slice(json_conv(poke_pull())))

def poke_pull():
    poke = input("""Choose a Pokemon!
> """)
    poke_api = f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}/"
    return poke_api

def json_conv(poke_api):
    poke_json = requests.get(poke_api)
    poke_json = poke_json.json()
    return poke_json

def api_slice(json2python): 
    poke_pic= json2python["sprites"]["front_shiny"]
    return poke_pic

def wget_pic(imagelink):
    wget.download(imagelink, '/home/captain/tlg_learning_python/')

main()