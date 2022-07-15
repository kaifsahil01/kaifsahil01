import aminofix
from BotAmino import *
from BotAmino import BotAmino
import sys
client = BotAmino("kaifsahil0000@gmail.com","bhai+sahil")
def is_staff(args):
    return args.authorId in ('5e9b879e-d9ae-4907-96ce-19d00c5c270c',"0358c9cd-cd60-43e8-b2ce-311435b5eec2")
@client.command("setw",condition=is_staff)
def setw(args):
    data = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId)
    reply_message = data.json['extensions']
    if reply_message:
        reply_message = data.json['extensions']['replyMessage']['content']
        args.subClient.set_welcome_message(reply_message)
    args.subClient.send_message(args.chatId, "Welcome wall message changed")
print("started...")
@client.command("hello",condition=is_staff)
def hello(data):
	data.subClient.send_message(data.chatId, message="""
hello
""")

client.launch("true")
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
