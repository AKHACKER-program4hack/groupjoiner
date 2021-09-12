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
        while True:
            try:
                joinedgroups = []
                alreadyjoined = []
                with open("grouptojoin.txt","r") as f:
                    groupstojoin = f.read().splitlines()
                    if groupstojoin == []:
                        continue
                    for group in groupstojoin:
                        if len(joinedgroups) == 5:
                            pass
                        elif len(joinedgroups) != 5:
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
                print("sleeping for 360 seconds")
                time.sleep(360)
            except Exception as error:
                if "A wait of " in str(error):
                    s = str(error).split()[3]
                    print("Sleeping for " + str(s) + " seconds to start again cause by telegram server")
                    time.sleep(int(s))
                else:
                    print(error)
                    continue
    Client.run_until_disconnected()
