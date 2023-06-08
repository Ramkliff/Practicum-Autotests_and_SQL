import requests
import data
import conf


# Крюков Александр. 5 когорта - финальный проект. инженер по тестированию плюс
def create_order():
    url = conf.URL + conf.create_order
    response = requests.post(url, json=data.body_create)
    return response


def test_success_get_order():
    response = create_order()
    assert response.status_code == 201

    track_number = response.json()['track']

    track_url = conf.URL + conf.get_order + "?t=" + str(track_number)
    response = requests.get(track_url)

    assert response.status_code == 200

    if response.status_code == 200:
        print("Тест пройден")
    else:
        print("Тест провален")


test_success_get_order()
