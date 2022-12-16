from pokemon_type import *
import pdb
import pokebase as pb
import json
import requests
def main():
    possible_types = find_best_offensive()
    total_types = []
    for lst in possible_types:
        for ty in lst:
            if ty not in total_types:
                total_types.append(ty)
    total_types = [typ.lower() for typ in total_types]
    poss = get_poss(total_types, only_two=True)

    with open("possible_pokemon.json", "w") as f:
        f.write(f"{len(poss)}\n")
        f.write(str(poss))

def filter_by_evolution(poss):
    """filters dictionary of pokemon by removing lower evolutions"""
    for name in poss:
        resp = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").content)
        pdb.set_trace()


def get_poss(possible_types, only_two=False):
    with open("download.json") as f:
        pokedex = json.loads(f.read())
    
    # for pokemon in pokedex["pokemon_entries"]:
        # print(pokemon['pokemon_species']['name'])
    poss = {}
    for typ in possible_types:
        resp = json.loads(requests.get(f"https://pokeapi.co/api/v2/type/{typ}").content)
        for pokemon in resp["pokemon"]:
            # pdb.set_trace()
            pokemon = pokemon["pokemon"]
            if "gmax" in pokemon["name"] or "mega" in pokemon["name"]:
                continue
            if pokemon["name"] in poss:
                poss[pokemon["name"]].append(typ)
            else:
                poss[pokemon["name"]] = [typ]
    if only_two:
        nw = {}
        for key in poss:
            if len(poss[key]) >= 2:
                nw[key] = poss[key]
        poss = nw
        
    poss = filter_by_evolution(poss)
                
    return poss
    
            
    


    



if __name__ == "__main__":
    main()