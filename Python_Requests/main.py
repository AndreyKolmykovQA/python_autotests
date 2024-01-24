"""
Python Requests Andrey Kolmykov
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'f1d31de7274e1eebfb71f921b5ade0b6'}
body = {
    "name": "generate",
    "photo": "generate"
}
body_2 = {
    "pokemon_id": "28420",
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers = HEADER, timeout = 5) # Создать покемона
json_data = response.json()
#print(f'Статус код: {response.status_code}). Сообщение: {response.json()["message"]}. ID покемона:')
print(response)
#json_data = response.json()

response = requests.put(url=f'{URL}/pokemons', json=body_2, headers = HEADER, timeout = 5) # Изменить данные покемона
print(response)

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body_2, headers = HEADER, timeout = 5) # Поймать в покебол
print(response)