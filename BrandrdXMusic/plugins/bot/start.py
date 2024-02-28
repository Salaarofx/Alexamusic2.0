import time

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch
import random 
import config
from BrandrdXMusic import app
from BrandrdXMusic.misc import _boot_
from BrandrdXMusic.plugins.sudo.sudoers import sudoers_list
from BrandrdXMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from BrandrdXMusic.utils.decorators.language import LanguageStart
from BrandrdXMusic.utils.formatters import get_readable_time
from BrandrdXMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

BACHHA_PICS = [
"https://telegra.ph/file/c777a8fba33ea23e20f02.jpg",
"https://telegra.ph/file/eb2a1b5875dbd87ad16b5.jpg",
"https://telegra.ph/file/eb360fb4e80d7bb08b941.jpg",
"https://telegra.ph/file/4f5d1d86be0a8b5e7d81d.jpg",
"https://telegra.ph/file/eceb13fc17b0150aa9cea.jpg",
"https://telegra.ph/file/6f3a8b5643d0ca82bd1f6.jpg",
"https://telegra.ph/file/9a12a9d6a9fea986f2ec7.jpg",
"https://telegra.ph/file/5d95a16a2ad07f59d1074.jpg",
"https://telegra.ph/file/4b6bd810600733e53d929.jpg",
"https://telegra.ph/file/4a2e606b2f6d02bf61cb7.jpg",
"https://telegra.ph/file/c9c2969b16e86552f5b55.jpg",
"https://telegra.ph/file/d8a1aa350aa7d93e66d82.jpg",
"https://telegra.ph/file/904140188f9b0fc489590.jpg",
"https://telegra.ph/file/42adebe71fa4257f39b75.jpg",
"https://telegra.ph/file/0be9952c86295cb8f78db.jpg",
"https://telegra.ph/file/9036592c9f9b7b6bbc08a.jpg",
"https://telegra.ph/file/f14e9ba47831e5c82749f.jpg",
"https://telegra.ph/file/a0ef1ac59c6a1d104da96.jpg",
"https://telegra.ph/file/5e678d026ab7a6ac1922b.jpg",
"https://telegra.ph/file/0946bc125e890361ae2c2.jpg",
"https://telegra.ph/file/e35abc8996bb0fab9aa48.jpg",
"https://telegra.ph/file/997baa16121e0455acfad.jpg",
"https://telegra.ph/file/43a1f6a3fd4f9508ed5e3.jpg",
"https://telegra.ph/file/9377dbd1bdcf6b2f8d5dc.jpg",
"https://telegra.ph/file/5c02f2f3bd91ef1ccda66.jpg",
"https://telegra.ph/file/4f1d1437891ccc80812bf.jpg",
"https://telegra.ph/file/06e3a538771d6fd7f0a9a.jpg",
"https://telegra.ph/file/b583bcce2c335319ba368.jpg",
"https://telegra.ph/file/d6b80d241d4b329426452.jpg",
"https://telegra.ph/file/e4be7ef8a4f9acb9afc89.jpg",
"https://telegra.ph/file/5dc8d5be84911a0fca74c.jpg",
"https://telegra.ph/file/94f4ec81a1ea567eda83d.jpg",
"https://telegra.ph/file/3ef00db7ff5e15c8efc54.jpg",
"https://telegra.ph/file/22d56cf312248f4fa6489.jpg",
"https://telegra.ph/file/f5b2ba114aa8d8bb902db.jpg",
"https://telegra.ph/file/6dad71099a13379f2068d.jpg",
"https://telegra.ph/file/683959013c0a4c93acbd9.jpg",
"https://telegra.ph/file/be98dea07f4b5938a4490.jpg",
"https://telegra.ph/file/becb2d28b38bffd33f6ca.jpg",
"https://telegra.ph/file/f3bfe1068542aeaa5fd7c.jpg",
"https://telegra.ph/file/fe4c74858d288d5c61e65.jpg",
"https://telegra.ph/file/a6ee40f2a954fdac9cb18.jpg",
"https://telegra.ph/file/86ee02ba743844f861333.jpg",
"https://telegra.ph/file/158353fb837ca6ee8a77e.jpg",
]

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                       photo=random.choice(BACHHA_PICS),
                       caption=_["help_1"].format(config.SUPPORT_CHAT), reply_markup=keyboard
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        await message.reply_photo(
            photo=random.choice(BACHHA_PICS),
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo=random.choice(BACHHA_PICS),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
