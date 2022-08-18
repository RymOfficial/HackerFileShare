import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝗛𝗲𝗹𝗹𝗼 {first}\n\n𝗜 𝗖𝗮𝗻 𝗦𝘁𝗼𝗿𝗲 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗙𝗶𝗹𝗲𝘀 𝗶𝗻 𝗦𝗽𝗲𝗰𝗳𝗶𝗲𝗱 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗔𝗻𝗱 𝗢𝘁𝗵𝗲𝗿 𝗨𝘀𝗲𝗿𝘀 𝗖𝗮𝗻 𝗔𝗰𝗲𝘀𝘀 𝗜𝘁 𝗙𝗿𝗼𝗺 𝗦𝗽𝗲𝗰𝗶𝗮𝗹 𝗟𝗶𝗻𝗸\n\n𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗕𝘆 @RYMOFFICIAL.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {first}\n\nYᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ")

#set your Custom Caption here, Keep None for Disable Custom Caption
default_custom_caption = """
📁 @RymOfficial {file_caption}
★━━━━━━ ⊛ 🇮🇳 ⊛ ━━━━━━★
╔══⚘⚚ Jᴏɪɴ Oᴜʀ Nᴇᴛᴡᴏʀᴋ ⚘⚚═══╗
☞ Nᴇᴛᴡᴏʀᴋ @RymOfficial         ☜
☞ Mᴏᴠɪᴇs @SonalModdingGod      ☜
☞ Sᴜᴘᴘᴏʀᴛ @JaiHindChatting     ☜
╚══⚘⚚ Jᴏɪɴ Oᴜʀ Nᴇᴛᴡᴏʀᴋ ⚘⚚═══╝
♥️ 𝗧𝗲𝗮𝗺 ➜ [𝐑𝐲𝐦 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥]
★━━━━━━ ⊛ 🇮🇳 ⊛ ━━━━━━★
"""
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", default_custom_caption)

#set True if you want to prevent users from forwarding files from bot
if os.environ.get("PROTECT_CONTENT", None) == 'True':
    PROTECT_CONTENT = True
else:
    PROTECT_CONTENT = False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5038784553)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
