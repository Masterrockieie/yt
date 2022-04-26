from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group", url="https://t.me/kerala_status_downloader"),
         InlineKeyboardButton(
            "Owner", url="https://t.me/Unni0240")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n My name is ,i can download you tube vidoe & Audio "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
