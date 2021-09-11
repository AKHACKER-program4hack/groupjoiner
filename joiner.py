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
                    if len(joinedgroups) == 3:
                        break
                    elif len(joinedgroups) != 3:
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


#Updates(updates=[], users=[], chats=[Channel(id=1567490931, title='1', photo=ChatPhotoEmpty(), date=datetime.datetime(2021, 9, 10, 13, 28, 50, tzinfo=datetime.timezone.utc), version=0, creator=False, left=False, broadcast=False, verified=False, megagroup=True, restricted=False, signatures=False, min=False, scam=False, has_link=False, has_geo=False, slowmode_enabled=True, access_hash=8539590535293599179, username='test123456gagaha', restriction_reason=[], admin_rights=None, banned_rights=None, default_banned_rights=ChatBannedRights(until_date=datetime.datetime(2038, 1, 19, 3, 14, 7, tzinfo=datetime.timezone.utc), view_messages=False, send_messages=False, send_media=False, send_stickers=False, send_gifs=False, send_games=False, send_inline=False, embed_links=False, send_polls=False, change_info=True, invite_users=False, pin_messages=True), participants_count=None)], date=datetime.datetime(2021, 9, 10, 13, 29, 42, tzinfo=datetime.timezone.utc), seq=0)