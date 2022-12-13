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
    poss = get_poss(total_types)

    with open("possible_pokemon.json", "w") as f:
        f.write(str(poss))



def get_poss(possible_types):
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
            if pokemon["name"] in poss:
                poss[pokemon["name"]].append(typ)
            else:
                poss[pokemon["name"]] = [typ]
    return poss
    
            
    


    



if __name__ == "__main__":
    main()