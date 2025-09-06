import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 13797618
API_HASH = "75868664d4d7f432c8b40d90dd096687"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8285500958:AAGvoBt7mZl5gL8UvKQaTnnsk-yqBr1R1kc"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://sahdeepyadav570_db_user:sahdeepyadav570_db_user@cluster0.mz7ds9g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002680089693

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 8048829396

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/Naruto_shippuden_in_Hindidubbeds"
SUPPORT_GROUP = "https://t.me/sahdeepyadav52"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQDSiPIAvsYkPgsgNCCTAYTLzwwLokUSozw5YERYIgBsCo3_lRBykRZWYxjHOKh8-3EGuooDlajlLdqZVfK94nRul2TQBJTylC4f0gLPnQiSqTmK5LT37pZc3NAhlXGouaeu_LAF8yAbo45gTjJuEf5kOetGA3WhAFLnzNbqZrrGhgEBMf5gyCVfiUd4H8iV9ZT-7DKfIiXPJvAs0KhFGz35CUVIXAqpDmhuVwYiNNqZip4ubObEiOw44HN0HtUqeoDNUGl59zqzh1I4of2bvpCfIpLbeerh1GgGF0f2dRrs2v26YUoxgA6qCfvSW7V_UU4SJG3dnNfzTeffBD2gvYRIuLeKFAAAAAHfv2PUAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"

PING_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
STATS_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
STREAM_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/36c6d5345a4c2eb76e3df-ee17c6985412f46d33.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )

