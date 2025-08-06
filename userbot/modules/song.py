from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot.language import get_value
LANG = get_value("song")

@register(outgoing=True, pattern="^.deez(\d*|)(?: |$)(.*)")
async def deezl(event):
    if event.fwd_from:
        return
    sira = event.pattern_match.group(1)
    if sira == '':
        sira = 0
    else:
        sira = int(sira)
    mahni = event.pattern_match.group(2)
    if len(mahni) < 1:
        if event.is_reply:
            sarki = await event.get_reply_message().text
        else:
            await event.edit(LANG['GIVE_ME_SONG']) 
    await event.edit(LANG['SEARCHING'])
    chat = "@DeezerMusicBot"
    async with bot.conversation(chat) as conv:
        try:     
            mesaj = await conv.send_message(str(randint(31,62)))
            mahnilar = await conv.get_response()
            await mesaj.edit(mahni)
            mahnilar = await conv.get_response()
        except YouBlockedUserError:
            await event.reply(LANG['BLOCKED_DEEZER'])
            return
        await event.client.send_read_acknowledge(conv.chat_id)
        if mahnilar.audio:
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, LANG['UPLOADED_WITH'], file=mahnilar.message)
            await event.delete()
        elif mahnilar.buttons[0][0].text == "No results":
            await event.edit(LANG['NOT_FOUND'])
        else:
            await mahnilar.click(sira)
            mahni = await conv.wait_event(events.NewMessage(incoming=True,from_users=595898211))
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, f"`{mahnilar.buttons[sira][0].text}` | " + LANG['UPLOADED_WITH'], file=mahni.message)
            await event.delete()


CmdHelp('song').add_command('deez', '<mahnı adı>', 'Deezerdən mahnı atar.').add()
