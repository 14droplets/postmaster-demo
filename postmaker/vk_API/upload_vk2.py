import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from toks import main_token

vk_session = vk_api.VkApi(token = main_token)
session_api = vk_session.get_api()

def send(msg):
    session_api.messages.send(user_id = 677649289, message = msg, random_id = 0)

while True:
    send(input())


