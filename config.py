"""Bot configuration variables."""
from os import environ, getenv, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

# Environment
ENVIRONMENT = getenv("ENVIRONMENT")

# Chatango rooms
CHATANGO_TEST_ROOM = getenv("CHATANGO_TEST_ROOM")
CHATANGO_ACLEE_ROOM = getenv("CHATANGO_ACLEE_ROOM")
CHATANGO_BLAB_ROOM = getenv("CHATANGO_BLAB_ROOM")
CHATANGO_SIXERS_ROOM = getenv("CHATANGO_SIXERS_ROOM")
CHATANGO_EAGLES_ROOM = getenv("CHATANGO_EAGLES_ROOM")
CHATANGO_PHILLIES_ROOM = getenv("CHATANGO_PHILLIES_ROOM")
CHATANGO_NFL_ROOM = getenv("CHATANGO_NFL_ROOM")
CHATANGO_OBI_ROOM = getenv("CHATANGO_OBI_ROOM")
CHATANGO_DUBS_ROOM = getenv("CHATANGO_DUBS_ROOM")
CHATANGO_REDZONE_ROOM = getenv("CHATANGO_REDZONE_ROOM")
CHATANGO_FLYERS_ROOM = getenv("CHATANGO_FLYERS_ROOM")
CHATANGO_ROOMS = [
    # CHATANGO_TEST_ROOM,
    CHATANGO_ACLEE_ROOM,
    # CHATANGO_SIXERS_ROOM,
    CHATANGO_PHILLIES_ROOM,
    CHATANGO_FLYERS_ROOM,
    CHATANGO_EAGLES_ROOM,
    CHATANGO_NFL_ROOM,
    CHATANGO_OBI_ROOM,
    CHATANGO_REDZONE_ROOM,
]

# Chatango credentials
CHATANGO_BOT_USERNAME = getenv("CHATANGO_BOT_USERNAME")
CHATANGO_BOT_PASSWORD = getenv("CHATANGO_BOT_PASSWORD")
CHATANGO_BRO_USERNAME = getenv("CHATANGO_BRO_USERNAME")
CHATANGO_BRO_PASSWORD = getenv("CHATANGO_BRO_PASSWORD")

# Chatango users access to protected commands
CHATANGO_SPECIAL_USERS = getenv("CHATANGO_SPECIAL_USERS")
if CHATANGO_SPECIAL_USERS:
    CHATANGO_SPECIAL_USERS = CHATANGO_SPECIAL_USERS.split(",")

# Database
DATABASE_URI = getenv("DATABASE_URI")
DATABASE_COMMANDS_TABLE = getenv("DATABASE_COMMANDS_TABLE")
DATABASE_WEATHER_TABLE = getenv("DATABASE_WEATHER_TABLE")
DATABASE_ARGS = {"ssl": {"ca": f"{BASE_DIR}/creds/ca-certificate.crt"}}

# Google Cloud
GOOGLE_APPLICATION_CREDENTIALS = "gcloud.json"
GOOGLE_BUCKET_NAME = getenv("GOOGLE_BUCKET_NAME")
GOOGLE_BUCKET_URL = getenv("GOOGLE_BUCKET_URL")

# Gifs
GIPHY_API_KEY = getenv("GIPHY_API_KEY")
GFYCAT_CLIENT_ID = getenv("GFYCAT_CLIENT_ID")
GFYCAT_CLIENT_SECRET = getenv("GFYCAT_CLIENT_SECRET")
REDGIFS_ACCESS_KEY = getenv("REDGIFS_ACCESS_KEY")

# Stock
IEX_API_TOKEN = getenv("IEX_API_TOKEN")
IEX_API_BASE_URL = "https://cloud.iexapis.com/stable/stock/"

# Crypto
ALPHA_VANTAGE_API_KEY = environ.get("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_PRICE_BASE_URL = "https://api.cryptowat.ch/markets/bitfinex/"
ALPHA_VANTAGE_CHART_BASE_URL = "https://www.alphavantage.co/query/"

# Plotly
PLOTLY_API_KEY = getenv("PLOTLY_API_KEY")
PLOTLY_USERNAME = getenv("PLOTLY_USERNAME")
PLOTLY_ALT_API_KEY = getenv("PLOTLY_ALT_API_KEY")
PLOTLY_ALT_USERNAME = getenv("PLOTLY_ALT_USERNAME")

# Weather
WEATHERSTACK_API_KEY = getenv("WEATHERSTACK_API_KEY")
METRIC_SYSTEM_USERS = getenv("METRIC_SYSTEM_USERS")

# Email
GMAIL_EMAIL = getenv("GMAIL_EMAIL")
GMAIL_PASSWORD = getenv("GMAIL_PASSWORD")

# Twilio
TWILIO_SENDER_PHONE = getenv("TWILIO_SENDER_PHONE")
TWILIO_RECIPIENT_PHONE = getenv("TWILIO_RECIPIENT_PHONE")
TWILIO_AUTH_TOKEN = getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = getenv("TWILIO_ACCOUNT_SID")

# Reddit
REDDIT_CLIENT_ID = getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = getenv("REDDIT_CLIENT_SECRET")
REDDIT_PASSWORD = getenv("REDDIT_CLIENT_SECRET")

# Rapid API
RAPID_API_KEY = getenv("RAPID_API_KEY")

# IP Data
IP_DATA_KEY = getenv("IP_DATA_KEY")

# Instagram
INSTAGRAM_USERNAME = getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = getenv("INSTAGRAM_PASSWORD")
INSTAGRAM_APP_ID = getenv("INSTAGRAM_APP_ID")
INSTAGRAM_APP_SECRET = getenv("INSTAGRAM_APP_SECRET")
