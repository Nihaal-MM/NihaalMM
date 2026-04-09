import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)


    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed{response.status_code}")

pokemon_name = input(str("Pokemon Name :"))
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    height = int(pokemon_info["height"])*10
    weight = int(pokemon_info["weight"])/10
    abilities_inp = pokemon_info["abilities"]
    abilities_list_raw = []
    for i in abilities_inp:
        abi_dict = i["ability"]
        name = abi_dict["name"]
        abilities_list_raw.append(name)

    seperator = " , "
    abilities_list = seperator.join(abilities_list_raw)
    print(f"Name : {pokemon_info["name"]}".capitalize())
    print(f"Id : {pokemon_info["id"]}")
    print(f"Height : {height} cm")
    print((f"Weight : {weight} kg"))
    print(f"Key abilities : {abilities_list}")
