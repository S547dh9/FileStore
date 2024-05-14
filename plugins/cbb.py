#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴢxᴄ</a>\n○ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/FLEX_BOTS_NEWS'>FʟᴇX Bᴏᴛs</a>\n○ ᴀɴɪᴍᴇ Hɪɴᴅɪ  Cʜᴀɴɴᴇʟ : <a href='https://t.me/ANIME_BARLOW'>Aɴɪᴍᴇ Bᴀʀʟᴏᴡ</a>\n○ ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ Cʜᴀɴɴᴇʟ : <a href='https://t.me/Ongoing_Anime_Barlow'>Oɴɢᴏɪɴɢ Aɴɪᴍᴇ Bᴀʀʟᴏᴡ </a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/EMXES_COMMUNITY'>Eᴍxᴇs Cᴏᴍᴍᴜɴɪᴛʏ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ɴᴇᴛᴡᴏʀᴋ', url='https://t.me/Emxes_Network')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


#⋗  ᴛᴇʟᴇɢʀᴀᴍ - @Codeflix_bots

#- ᴄʀᴇᴅɪᴛ - Github - @Codeflix-bots , @erotixe
#- ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
#- ᴛʜᴀɴᴋ ʏᴏᴜ ᴄᴏᴅᴇғʟɪx ʙᴏᴛs ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
#- ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ @Codeflix-bots  
#- ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ -> ᴛᴇʟᴇɢʀᴀᴍ @codeflix_bots Community @Otakflix_Network </b>
