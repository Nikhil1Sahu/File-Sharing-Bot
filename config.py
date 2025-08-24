# (©)OwnerOfNG
import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# ===================== Bot & API Config =====================
TG_BOT_TOKEN = os.environ.get(
    "TG_BOT_TOKEN", "8375007513:AAF2J8ItNJSAq4WAiLN-TXlfMcwMg4Wk_aE"
)
APP_ID = int(os.environ.get("APP_ID", "18466881"))
API_HASH = os.environ.get("API_HASH", "8c8ca14ad8e416ce4e6ea717db7ec6af")

# Database channel
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@NG_botz")

# Owner ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5565120414"))

# Port
PORT = os.environ.get("PORT", "8080")

# ===================== Database Config =====================
DB_URI = os.environ.get(
    "DATABASE_URL",
    "mongodb+srv://nikhilsahu7j:dTQKfvo0jABOYKOu@cluster0.n2csgvi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ===================== Force Sub Config =====================
# List of channel usernames or URLs separated by space in .env
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "@manhwa_kingdom")
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", "True") == "true" else false

# ===================== Bot Workers =====================
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "3"))

# ===================== Start Message Config =====================
START_PIC = os.environ.get(
    "START_PIC", "https://envs.sh/uxs.jpeg"
)
START_MSG = os.environ.get(
    "START_MESSAGE",
    "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link."
)

# ===================== Admins Config =====================
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "1918675169 8190474898").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Always include the owner
ADMINS.append(OWNER_ID)
ADMINS.append(5565120414)

# ===================== Force Sub Message =====================
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>"
)

# ===================== Other Bot Config =====================
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False") == "true" else false
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "180"))
AUTO_DELETE_MSG = os.environ.get(
    "AUTO_DELETE_MSG",
    "This file will be automatically deleted in 3mins. Please ensure you have saved any necessary content before this time."
)
AUTO_DEL_SUCCESS_MSG = os.environ.get(
    "AUTO_DEL_SUCCESS_MSG",
    "Your file has been successfully deleted. Thank you for using our service. ✅"
)
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == 'true'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

# ===================== Logging Config =====================
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
