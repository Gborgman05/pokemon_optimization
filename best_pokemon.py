from pokemon_type import *
import pokebase as pb
def main():
    possible_types = find_best_offensive()
    pokedex = pb.pokedex('galar')  # Quick lookup.
    poss = get_poss(pokedex, possible_types[0])
    print(poss)



def get_poss(pokedex, possible_types):
    poss_pokemon = {}
    count = 0
    for pokemon in pokedex.pokemon_entries:
        print(f"pokemon {count}")
        pokemon = pb.pokemon(pokemon.pokemon_species.name)
        for ty in pokemon.types:
            if ty.type in possible_types:
                poss_pokemon[pokemon.name] = [t.type for t in pokemon.types]
                break
    return poss_pokemon
        

    



if __name__ == "__main__":
    main()