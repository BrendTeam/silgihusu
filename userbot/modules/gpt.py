# SilgiUserbot məhsuludur əkmə peysərin balası
from telethon import events
from userbot import bot
from g4f.client import Client
from userbot.events import register
from userbot.cmdhelp import CmdHelp

client = Client()

@register(outgoing=True, pattern=r"^\.gpt (.+)")
async def gpt_plugin(event):
    mesaj = event.pattern_match.group(1)
    await event.edit("⏳ Cavab axtarılır...")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": mesaj}],
            web_search=True
        )

        gpt_response = response.choices[0].message.content
        await event.edit(f"**GPT Cavabı:**\n{gpt_response}")

    except Exception as e:
        await event.edit(f"Xəta baş verdi:\n`{str(e)}`")


@register(outgoing=True, pattern=r"^\.igpt (.+)")
async def igpt_plugin(event):
    mesaj = event.pattern_match.group(1)
    await event.edit("⏳ Şəkil axtarılır...")

    try:
        image_response = client.images.generate(
            model="flux",
            prompt=mesaj,
            response_format="url"
        )

        image_url = image_response.data[0].url
        await event.edit("Şəkil tapıldı!")
        await event.respond("**Generated Image:**", file=image_url)

    except Exception as e:
        await event.edit(f"Xəta baş verdi:\n`{str(e)}`")
CmdHelp('chatgpt').add_command(
    'gpt', 'sual', 'ChatGPT nin UserBot versiyası məsələn .gpt SilgiUserbot niyə ən yaxşı userbotdur?'
).add_command(
    'igpt', 'şəkil', 'Yazdığınız şəkli yaradar'
).add_info(
    'BrendUserbot Məhsuludur'
).add()
