from pokemon_type import *
import pdb
import pokebase as pb
def main():
    possible_types = find_best_offensive()
    pokedex = pb.pokedex('national')  # Quick lookup.
    total_types = []
    for lst in possible_types:
        for ty in lst:
            if ty not in total_types:
                total_types.append(ty)
    total_types = [typ.lower() for typ in total_types]
    poss = get_poss(pokedex, total_types)

    with open("possible_pokemon.json", "w") as f:
        f.write(str(poss))



def get_poss(pokedex, possible_types):
    poss_pokemon = {}
    count = 0
    for pokemon in pokedex.pokemon_entries:
        count += 1
        pokemon = pb.pokemon(pokemon.pokemon_species.name)
        print(f"pokemon: {pokemon.name}, number {count}")
        # pdb.set_trace()
        f = open("possible_pokemon.json", "w+")
        for ty in pokemon.types:
            if ty.type.name in possible_types:
                f.write 
                poss_pokemon[pokemon.name] = [t.type.name for t in pokemon.types]
                break
    return poss_pokemon
        

    



if __name__ == "__main__":
    main()