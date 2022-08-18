import os
import aminofix as amino
from BotAmino import *
from BotAmino import BotAmino
import sys
client = BotAmino("sa4646848@gmail.com","KAIF@321456")
def is_staff(args):
    return args.authorId in ('5e9b879e-d9ae-4907-96ce-19d00c5c270c',"08083279-cb7a-4cce-aff6-9b1e01952691")
blacklistedUsers = ["shy","lol"]
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
print("done")
def check_new_member(self):
        if not (self.message_bvn or self.welcome_chat):
            return
        new_list = self.get_all_users(start=0, size=25, type="recent")
        new_member = [(elem["nickname"], elem["uid"]) for elem in new_list.json["userProfileList"]]
        for elem in new_member:
            name, uid = elem[0], elem[1]
            if name == "blacklistedUsers":
            	self.ban(userId=uid,reason="Spam Account in Recent Members")

            val = self.get_wall_comments(userId=uid, sorting='newest').commentId

            if not val and self.message_bvn:
                with suppress(Exception):
                    self.comment(message=self.message_bvn, userId=uid)

            if not val and self.welcome_chat:
                with suppress(Exception):
                    self.send_message(chatId=self.welcome_chat, message=f"Welcome here ‎‏‎‏@{name}!‬‭", mentionUserIds=[uid])

        new_users = self.get_all_users(start=0, size=30, type="recent")
        self.new_users = [elem["uid"] for elem in new_users.json["userProfileList"]]

def welcome_new_member(self):
        new_list = self.get_all_users(start=0, size=25, type="recent")
        new_member = [(elem["nickname"], elem["uid"]) for elem in new_list.json["userProfileList"]]
        for elem in new_member:
            name, uid = elem[0], elem[1]
            if name == "blacklistedUsers":
            	self.ban(userId=uid,reason="Spam Account in Recent Members")
            val = self.get_wall_comments(userId=uid, sorting='newest').commentId
print("done")
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
