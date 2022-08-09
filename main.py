import os
from os import sys
import samino
from time import sleep
from os import path
import requests
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.GREEN + style.BOLD)
print(pyfiglet.figlet_format(" marshal", font="digital"))
print(pyfiglet.figlet_format("CoHost Spam", font="small"))
f='━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
client = samino.Client()
e="jtrmvft7h@1secmail.com"
p="786786"
client.login(e,p)
print("\nLogin Successfully")
print(f)
#keep_alive()
client.headers
chat="http://aminoapps.com/p/3astkgt"
config_chat = client.get_from_link(chat).json #You have  host on chat
thread_id = config_chat["linkInfo"]["objectId"]
ndc_id = config_chat["linkInfo"]["ndcId"]
local = samino.Local(comId = ndc_id)
community = "http://aminoapps.com/c/BTS_worldz_"
comId = client.get_from_link(community).comId
chat = client.get_from_link(chat)
print("# Getting all online members")
local = samino.Local(comId)
curators = local.get_all_users("curators").userId
leaders = local.get_all_users("leaders").userId
leaders.extend(curators)

for i in range(0, 2100, 100):
    users = local.get_online_users(i, 100).userId
    if users: leaders.extend(users)
    else: break


def remove_host(userId, comId, chatId, headers): print("#", requests.Session().delete(f"https://service.narvii.com/api/v1/x{comId}/s/chat/thread/{chatId}/co-host/{userId}", headers=headers).json()["api:message"])


print("# Starting\n")
for userId in leaders: remove_host(userId, chat.comId, chat.objectId, client.headers)
