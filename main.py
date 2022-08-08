import os
from os import sys
import samino
from time import sleep
from os import path
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
HostChatLink="http://aminoapps.com/p/3astkgt"
config_chat = client.get_from_link(HostChatLink).json #You have  host on chat
thread_id = config_chat["linkInfo"]["objectId"]
ndc_id = config_chat["linkInfo"]["ndcId"]
local = samino.Local(comId = ndc_id)
targetlink="http://aminoapps.com/p/xoxkzp"
remove = client.get_from_link(str(targetlink)).objectId
while True:
	print("boom 💥💥💥💥...")
	try:
		local.remove_host(chatId=thread_id, userId=remove)
	except:
		pass
