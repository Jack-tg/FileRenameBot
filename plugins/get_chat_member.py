import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import Client, Filters, ChatPermissions
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserBannedInChannel

@pyrogram.Client.on_message(pyrogram.Filters.command(["rename"]))
async def rename_doc(bot, update):
    try:
        chat = await bot.get_chat_member("@Zed1Projctz", update.chat.id)
        if chat.status=='kicked':
            if edit_message:
                await reply("You are Banned😌")
            return False
        else:
            return True

    except UserNotParticipant:
        if edit_message:
            await reply("Join @Zed1Projctz To Use Me")
    except UserBannedInChannel:
        if edit_message:
                await reply("You are Banned😌")
    except Exception:
        LOGGER.exception("Unable to verify user")
        if edit_message:
                await reply("Something wenr Wrong 😴")
    return False

