import sender_stand_request
import requests
import configuration

# Айгуль Кабламбаева, 22-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_track_order():
    track = sender_stand_request.get_new_order_track()
    track_response = requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER_PATH+"?t="+str(track))
    assert track_response.status_code == 200