from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt =<a href=https://t.me/kerala_status_downloader>Just send the link to the group</a>"
    await message.reply_text(helptxt)
