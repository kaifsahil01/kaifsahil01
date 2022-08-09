import samino
import requests

email = "jtrmvft7h@1secmail.com"  # email
password = "786786"  # password
chat = "http://aminoapps.com/p/3astkg"  # chat that you have host in it
community = "http://aminoapps.com/c/BTS_worldz_"  # community that you want to invite the online members of it

print("# Logging in")
client = samino.Client()
comId = client.get_from_link(community).comId
chat = client.get_from_link(chat)
client.login(email, password)
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
