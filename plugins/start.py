from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group 💫", url="https://t.me/kerala_status_downloader"),
         InlineKeyboardButton(
            "Owner ✨️", url="https://t.me/Unni0240")]
    ])
    
    welcomed = f"𝐻𝐸𝑌 <b>{message.from_user.first_name}</b>\n 𝐼 𝑐𝑎𝑛 𝑑𝑜𝑤𝑛𝑙𝑜𝑎𝑑 𝑦𝑜𝑢 𝑡𝑢𝑏𝑒 𝑣𝑖𝑑𝑒𝑜 & 𝐴𝑢𝑑𝑖𝑜"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
