from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group π«", url="https://t.me/kerala_status_downloader"),
         InlineKeyboardButton(
            "Owner β¨οΈ", url="https://t.me/Unni0240")]
    ])
    
    welcomed = f"π»πΈπ <b>{message.from_user.first_name}</b>\n πΌ πππ πππ€πππππ π¦ππ’ π‘π’ππ π£ππππ & π΄π’πππ"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
