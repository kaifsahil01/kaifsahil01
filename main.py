import aminofix
from BotAmino import *
from BotAmino import BotAmino
import threading
from threading import Thread
import sys
client = BotAmino("jtrmvft7h@1secmail.com","786786")
def is_staff(args):
    return args.authorId in ('5e9b879e-d9ae-4907-96ce-19d00c5c270c',"0358c9cd-cd60-43e8-b2ce-311435b5eec2","1dbe87e2-5293-4cb7-91fa-253f02cafd05")
@client.command("setw",condition=is_staff)
def setw(args):
    data = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId)
    reply_message = data.json['extensions']
    if reply_message:
        reply_message = data.json['extensions']['replyMessage']['content']
        args.subClient.set_welcome_message(reply_message)
    args.subClient.send_message(args.chatId, "Welcome wall message changed")
print("started...")
@client.command("hello")
def hello(data):
	data.subClient.send_message(data.chatId, message="""
hello
""")
#@client.on_all()
def on_message(data) -> None:
    content = data.message
    mtype = data.info.message.type
    if mtype != 0 and content and str(data.info.comId):
        data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
        data.subClient.send_message(data.chatId, f'Anti-Raid-Bot : MessageType {mtype} detected! Nickname: {data.author} | userId: {data.authorId} | messageId: {data.messageId}.')
        data.subClient.delete_message(data.chatId, data.messageId, asStaff=True, reason=f'Anti-Raid-Bot : MessageType {mtype} detected! Nickname: {data.author} | userId: {data.authorId} | messageId: {data.messageId}.')
        return
        try:
            data.subClient.ban(data.authorId, f'Anti-Raid-Bot : MessageType {mtype} detected! Nickname: {data.author} | userId: {data.authorId} | messageId: {data.messageId}.')
        except Exception:
            pass    

client.launch(True)
client.activity = "True"

################################################commands/команды################################################
time.sleep(10)
print("Bot started")
#socket
client.launch(True)
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()
