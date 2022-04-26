from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = Just send the link to the group
    await message.reply_text(helptxt)
