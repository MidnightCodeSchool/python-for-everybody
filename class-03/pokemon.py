# https://pokeapi.co/
# วิธีใช้
# https://pokeapi.co/api/v2/pokemon/ditto

import httpx
from rich import print
from rich.progress import track

def get_total_stat(data):
    """
    คำนวนค่า total stat ของ pokemon
    """
    data = data['stats']
    total = 0
    for stat in data:
        total += stat['base_stat']
    return total


pokemons = ['ditto', 'pikachu', 'mewtwo', 'mew', 'charizard', 'bulbasaur', 'squirtle', 'eevee', 'snorlax', 'dragonite']
pokemon_data = {}
for pokemon in track(pokemons):
    url = 'https://pokeapi.co/api/v2/pokemon' + '/' + pokemon
    r = httpx.get(url)
    data = r.json()
    total_stat = get_total_stat(data)
    pokemon_data[pokemon] = total_stat
# print(pokemon_data)
pokemon_with_most_stat = ""
most_stat = 0
for pokemon, total_stat in pokemon_data.items():
    print(f'{pokemon} total stat: {total_stat}')
    if total_stat > most_stat:
        most_stat = total_stat
        pokemon_with_most_stat = pokemon
print(f'Pokemon with most stat is {pokemon_with_most_stat} with total stat {most_stat}')
