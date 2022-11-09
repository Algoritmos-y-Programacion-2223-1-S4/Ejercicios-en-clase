from unicodedata import name
import requests
import json
from Pokemon import Pokemon

def main():
    url = "https://pokeapi.co/api/v2/pokemon-form"
    make_request(url)
    

def make_request(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemons = []
        payload = response.json()
        print(payload) 
        if payload.get("previous") == None:
            option = input("1. Next\n2. Exit\n")
            if option == "1":
                make_request(payload.get("next"))

        else:
            option = input("1. Next\n2. Previous\n3. Exit\n")
            if option == "1":
                make_request(payload.get("next"))
            elif option == "2":
                make_request(payload.get("previous"))
        

main()