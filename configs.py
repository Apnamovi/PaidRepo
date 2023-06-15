# (c) @LazyDeveloperr
import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "26461352"))
	API_HASH = os.environ.get("API_HASH", "ab9cc32776ada8335852b50cd96bb8c6")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "PermanentFileStoreBoT")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001637710147"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5069888600"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001847483358")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001745861668")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	LAZY_CHANNEL = int(os.environ.get('LAZY_CHANNEL', '-1001774877050'))
	LAZY_MODE = bool(os.environ.get("LAZY_MODE", True))
	LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/5e0d121c04318ce13a234.jpg")
	LP_BTN_MAIN_CH_USRNM = os.environ.get("LP_BTN_MAIN_CH_USRNM")
	LP_CHANNEL_USRNM = os.environ.get("LP_CHANNEL_USRNM")
	LPCH_ADMIN_USRMN = os.environ.get("LPCH_ADMIN_USRMN")
	LP_CUSTOM_TEMPLATE= os.environ.get("LP_CUSTOM_TEMPLATE")
  # LP_CUSTOM_TEMPLATE= os.environ.get("LP_CUSTOM_TEMPLATE","{file_name} - example \n\n Please Upadate this template acording to you @LazyDeveloperr ")
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
ᴛʜɪꜱ ɪꜱ ᴘᴇʀᴍᴀɴᴇɴᴛ ꜰɪʟᴇꜱ ꜱᴛᴏʀᴇ ʙᴏᴛ!
ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ɪ ᴡɪʟʟ ꜱᴀᴠᴇ ɪᴛ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ. ᴀʟꜱᴏ ᴡᴏʀᴋꜱ ꜰᴏʀ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴇᴅɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ɪ ᴡɪʟʟ ᴀᴅᴅ ꜱᴀᴠᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ꜰɪʟᴇ ɪɴ ᴄʜᴀɴɴᴇʟ & ᴀᴅᴅ ꜱʜᴀʀᴀʙʟᴇ ʙᴜᴛᴛᴏɴ ʟɪɴᴋ.

🤖 **ᴍʏ ɴᴀᴍᴇ:** [ꜰɪʟᴇꜱ ꜱᴛᴏʀᴇ ʙᴏᴛ](https://t.me/{BOT_USERNAME})

📝 **ʟᴀɴɢᴜᴀɢᴇ:** [PУΓHФИ3](https://www.python.org)

📚 **ʟɪʙʀᴀʀʏ:** [P͢y͢r͢o͢g͢r͢a͢m͢](https://docs.pyrogram.org)

📡 **ʜᴏꜱᴛᴇᴅ ᴏɴ:** [H͢e͢r͢o͢k͢u͢](https://heroku.com)

🧑🏻‍💻 **DΞVΞLФPΞЯ:** [J͎k͎ D͎e͎v͎e͎l͎o͎p͎e͎r͎](https://t.me/LazyDeveloperr)
"""
	ABOUT_DEV_TEXT = f"""
ᴀʟꜱᴏ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛꜱ ꜰʀᴏᴍ ᴅᴀᴛᴀʙᴀꜱᴇ. ꜱᴏ ʙᴇᴛᴛᴇʀ ᴅᴏɴ'ᴛ ꜱᴛᴏʀᴇ ᴛʜᴏꜱᴇ ᴋɪɴᴅ ᴏꜰ ᴛʜɪɴɢꜱ.
"""
	LAZY_HOME_TEXT = """
HΞУ, [{}](tg://user?id={})\n\nɪ'ᴍ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ **ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ**.

ミ★ 𝘚𝘦𝘯𝘥 𝘮𝘦 𝘢𝘯𝘺 𝘧𝘪𝘭𝘦 𝘐 𝘸𝘪𝘭𝘭 𝘨𝘪𝘷𝘦 𝘺𝘰𝘶 𝘢 𝘱𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵 𝘚𝘩𝘢𝘳𝘢𝘣𝘭𝘦 𝘓𝘪𝘯𝘬. 𝘐 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘈𝘭𝘴𝘰! 𝘊𝘩𝘦𝘤𝘬 **A͢b͢o͢u͢t͢ B͢o͢t͢**  𝘉𝘶𝘵𝘵𝘰𝘯 .

«[⚡️𝙇𝙖𝙯𝙮 𝙢𝙤𝙙𝙚 𝙨𝙩𝙖𝙩𝙪𝙨 : 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋✅]»
 🥷 𝘕𝘰𝘸 𝘌𝘷𝘦𝘳𝘺𝘵𝘩𝘪𝘯𝘨 𝘪𝘴 𝘶𝘱𝘰𝘯 𝘮𝘦 🥷
"""
	HOME_TEXT = """
HΞУ, [{}](tg://user?id={})\n\nɪ'ᴍ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ **ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ**.

ミ★ 𝘚𝘦𝘯𝘥 𝘮𝘦 𝘢𝘯𝘺 𝘧𝘪𝘭𝘦 𝘐 𝘸𝘪𝘭𝘭 𝘨𝘪𝘷𝘦 𝘺𝘰𝘶 𝘢 𝘱𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵 𝘚𝘩𝘢𝘳𝘢𝘣𝘭𝘦 𝘓𝘪𝘯𝘬. 𝘐 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘈𝘭𝘴𝘰! 𝘊𝘩𝘦𝘤𝘬 **A͢b͢o͢u͢t͢ B͢o͢t͢**  𝘉𝘶𝘵𝘵𝘰𝘯 .

«[⚡️𝙇𝙖𝙯𝙮 𝙢𝙤𝙙𝙚 𝙨𝙩𝙖𝙩𝙪𝙨 : 𝘋𝘐𝘚𝘈𝘉𝘓𝘌𝘋💢]»
 😏𝙣𝙤𝙬 𝙞𝙩𝙨 𝙖𝙡𝙡 𝙪𝙥𝙤𝙣 𝙪 𝙗𝙖𝙗𝙮👍
"""
