import requests

url = "https://pokeapi.co/api/v2/pokemon/130"

response = requests.get(url)
pokemon = response.json()

for item in pokemon['abilities']:
    ability_url = item['ability']['url']
    response_for_ability = requests.get(ability_url)
    ability = response_for_ability.json()
    print(ability)