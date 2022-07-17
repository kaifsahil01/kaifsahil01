from os import system
from os import system as sys
sys("pip install amino.fix==2.2.12")
import aminofix
from threading import Thread as t
import threading
client=aminofix.Client()
email="858otw0fqqpq@bheps.com"
password="786786"
client.login(email=email,password=password)
print("Connecté.")

chatlink=("http://aminoapps.com/p/8luxhii'")
chatinfo=client.get_from_code(chatlink)
chatId=chatinfo.objectId
comId=chatinfo.path[1:chatinfo.path.index('/')]
print (chatId)
print (comId)

subclient = aminofix.SubClient(comId=comId, profile=client.profile)

user_link=["http://aminoapps.com/p/198k7z","http://aminoapps.com/p/40tp4o"]
print(user_link)
I=[]
def lag(dum):
	for i in user_link:
		try:
			uid=client.get_from_code(i).objectId
			I.append(uid)
			print(uid)
			subclient.edit_chat(chatId=chatId,coHosts=I)
		except:
				print("co host as set")
				
def cohost():
	while True:
		t(target=lag,args=(1,)).start()
cohost()
