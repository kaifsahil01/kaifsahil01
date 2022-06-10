import sys
import copy
import zipfile
import os
from time import sleep
from json import dumps, load
from threading import Thread
import threading
from pathlib import Path
from contextlib import suppress
from string import punctuation
from unicodedata import normalize
import time
import urllib
import json
#from pdf2image import convert_from_path
#from youtube_dl import YoutubeDL
from BotAmino import *
import random

client=BotAmino(email = "jenlisak724@gmail.com",password = "kaif_sahil_21")


Device = "32420E76071FF35107EED65D0616CD34BDB4E076B8584BBD79B89DB6BB52814172D273021237E5ADE5"

header  = {"NDCDEVICEID": Device}
header["NDCAUTH"] = f"sid={client.sid}"
header["Content-Type"] = "application/octet-stream"
def is_staff(args):
    return args.authorId in ('1dbe87e2-5293-4cb7-91fa-253f02cafd05','')
def Get_UrlZip_From_Message(d,comId,chatId,messageId):
	if int(comId) == 0:
		info = d.get_message_info(chatId=chatId,messageId=messageId).json
	else:
		#sub = data.subClient(comId,profile=client.profile)
		info =d.get_message_info(chatId=chatId,messageId=messageId).json
	ZipUrl = info["chatBubble"]["resourceUrl"]
	return ZipUrl

def SaveOrgBubble():
	try:
		open("org.zip").close()
	except FileNotFoundError:
		Bytes = requests.get("http://cb1.narvii.com/packages/8062/0c65bfe8bafe1efea9ea0e47280e403848cadfb9.zip").content
		file = open("org.zip","wb")
		file.write(Bytes)
		file.close()

def SaveNewBubble(Url):
	Bytes = requests.get(Url).content
	file = open("New.zip","wb")
	file.write(Bytes)
	file.close()

def CreateZip1(ReColor = False):
	api = "https://service.narvii.com/api/v1/g/s/media/upload/target/chat-bubble-thumbnail"
	headers = header
	headers["Content-Type"] = "image/*"
	Zip = zipfile.ZipFile("org.zip","r")
	Zip.extract("background.png")
	Zip = zipfile.ZipFile("New.zip","r")
	names = Zip.namelist()
	if str(names).count('.gif') > 1:
		print("\n Cannot Copy Bubble !")
	else:
		for name in set(names):
			if name.endswith(".gif") == True or name.endswith(".png") == True:
				ImgName = name
				Bytes = Zip.open(ImgName).read()
				Url = requests.post(api,headers=headers,data=Bytes).json()["mediaValue"]
		os.rename("background.png",ImgName)
		Zip.extract("config.json")
		file = open("config.json","r")
		data = json.load(file)
		data["name"] = "Banned#BubbleCopy"
		data["previewBackgroundUrl"] = Url
		data["coverImage"] = Url
		if ReColor:
			print("\n Enter Code Like This : #000000")
			color = input(" Color Code : ")
			linkColor = input(" linkColor Code : ")
			if color: data["color"] = color
			if linkColor: data["linkColor"] = linkColor
		file = open("config.json","w")
		data = json.dumps(data)
		file.write(data)
		file.close()
		Zip = zipfile.ZipFile("OldBubble.zip","w")
		Zip.write(ImgName)
		Zip.write("config.json")
		Zip.close()
		return ImgName

def CreateZip2(ImgName):
	Zip = zipfile.ZipFile("New.zip","r")
	Zip.extract(ImgName)
	Zip = zipfile.ZipFile("NewBubble.zip","w")
	Zip.write(ImgName)
	Zip.write("config.json")
	Zip.close()

def GenerateBubble():
	api1 = f"{client.api}/g/s/chat/chat-bubble/templates/71b41f1a-4c09-4e07-ac9e-18ef9bbbe65f/generate"
	data = open("OldBubble.zip","rb").read()
	res = requests.post(api1,headers=header,data=data)
	if res.status_code == 200 and res.json()["api:message"] == "OK":
		bubbleId = res.json()["chatBubble"]["bubbleId"]
		print(f"\n Template Done With Id ---> {bubbleId} \n")
		return bubbleId
		print(bubbleId)
	else:
		print('\n',res.json()["api:message"])

def Set_New_Bubble(bubbleId):
	api2 = f"{client.api}/g/s/chat/chat-bubble/{bubbleId}"
	data = open("NewBubble.zip","rb").read()
	res = requests.post(api2,headers=header,data=data)
	if res.status_code == 200 and res.json()["api:message"] == "OK":
		print(" Done Custom Bubble !")
	else:
		print('\n',res.json()["api:message"])

@client.command("ice",condition=is_staff)
def ok(data):
	d=data.subClient
	chatId = data.chatId
	comId = data.comId
	userId = data.authorId
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	messageId = info.json["extensions"]["replyMessageId"]
	print("\n Get Message Id Done !")
	ZipUrl =  Get_UrlZip_From_Message(d,comId,chatId,messageId)
	SaveOrgBubble()
	SaveNewBubble(ZipUrl)
	ImgName = CreateZip1()
	bubbleId = GenerateBubble()
	CreateZip2(ImgName)
	Set_New_Bubble(bubbleId)
	#data.subClient.apply_bubble(bubbleId=bubbleId,chatId=data.chatId,applyToAll=True)
	cb=open("chatb.txt","a+")
	cb.write(bubbleId+"\n")
	cb.close()
	data.subClient.send_message(data.chatId,message="Bubble Copied")
	print("\n Load Messages.. !")
		
client.launch(True)
def extra(uid : str):
    event=uuid4()
    data = {
        "reward":{"ad_unit_id":"255884441431980_807351306285288","credentials_type":"publisher","custom_json":{"hashed_user_id":f"{uid}"},"demand_type":"sdk_bidding","event_id":f"{event}","network":"facebook","placement_tag":"default","reward_name":"Amino Coin","reward_valid":"true","reward_value":2,"shared_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f","version_id":"1569147951493","waterfall_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f"},
        "app":{"bundle_id":"com.narvii.amino.master","current_orientation":"portrait","release_version":"3.4.33567","user_agent":"Dalvik\/2.1.0 (Linux; U; Android 10; G8231 Build\/41.2.A.0.219; com.narvii.amino.master\/3.4.33567)"},"date_created":1620295485,"session_id":"49374c2c-1aa3-4094-b603-1cf2720dca67","device_user":{"country":"US","device":{"architecture":"aarch64","carrier":{"country_code":602,"name":"Vodafone","network_code":0},"is_phone":"true","model":"GT-S5360","model_type":"Samsung","operating_system":"android","operating_system_version":"29","screen_size":{"height":2260,"resolution":2.55,"width":1080}},"do_not_track":"false","idfa":"7495ec00-0490-4d53-8b9a-b5cc31ba885b","ip_address":"","locale":"en","timezone":{"location":"Asia\/Seoul","offset":"GMT+09:00"},"volume_enabled":"true"}
        }

    headers={
        "cookies":"__cfduid=d0c98f07df2594b5f4aad802942cae1f01619569096",
        "authorization":"Basic NWJiNTM0OWUxYzlkNDQwMDA2NzUwNjgwOmM0ZDJmYmIxLTVlYjItNDM5MC05MDk3LTkxZjlmMjQ5NDI4OA=="
    }
    requests.post("https://ads.tapdaq.com/v4/analytics/reward",json=data, headers=headers)

@client.command("joy")
def tap(args):
  args.subClient.send_message(args.chatId,message="""[bc]done""")
  for _ in range(250):
    threading.Thread(target=extra(args.authorId))
print("done")
@client.command("fix",condition=is_staff)
def prefix(args):
    if args.message:
        args.subClient.set_prefix(args.message)
        args.subClient.send_message(args.chatId, f"prefix set as {args.message}")
@client.command("hello")
def test(data):
    data.subClient.send_message(data.chatId, f"sahil")
print("ready")

#socket
def socketRoot():
 j=0
 while True:
  if j>=100:
   print("Updating socket.......")
   os.execv(sys.executable, ['python'] + sys.argv)
   print("Socket updated")
   j=0
  j=j+1
  time.sleep(1)
socketRoot()
