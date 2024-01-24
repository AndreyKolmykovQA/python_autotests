import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'f1d31de7274e1eebfb71f921b5ade0b6'}

def test_get_trainers_list():
    """
    TEST-1 Запрос на получение списка тренеров присылает 200-ку
    """
    response = requests.get(url=f'{URL}/trainers', timeout = 15)
    assert response.status_code == 200, ''

def test_trainer_name_in_response():
    """
    TEST-2 Наличие имени тренера в списке
    """
    params = {'trainer_id': 4720}
    response = requests.get(f'{URL}/trainers', params=params)
    print(response.text)
    trainer_name = response.json().get('trainer_name', '')
    expected_trainer_name = 'Питонист'
    assert trainer_name == expected_trainer_name, ''