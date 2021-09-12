from telethon.sync import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import functions, types
from config import api_hash, api_id
import time

with TelegramClient('anon', api_id, api_hash) as Client:
    print("stared")
    @Client.on(events.NewMessage(pattern=".joingroups",outgoing=True))
    async def get_groups(event):
        try:
            joinedgroups = []
            alreadyjoined = []
            with open("grouptojoin.txt","r") as f:
                groupstojoin = f.read().splitlines()
                for group in groupstojoin:
                    # group = "https://t.me/test123456gagaha"
                    if len(joinedgroups) == 20:
                        break
                    elif len(joinedgroups) != 20:
                        n = await Client(JoinChannelRequest(group))
                        if n.updates:
                            print("Joined")
                            joinedgroups.append(group)
                            groupstojoin.remove(group)
                        elif n.updates == []:
                            print("already joined")
                            alreadyjoined.append(group)
                            groupstojoin.remove(group)
            with open("grouptojoin.txt","w") as g:
                for group in groupstojoin:
                    g.write(group + "\n")
                
                
                
            
        except Exception as error:
            print(error)

    Client.run_until_disconnected()
