import os
import pathlib

from dotenv import load_dotenv

load_dotenv(pathlib.Path(__file__).parent.parent / '.env')

config = {
    "bot_token": os.getenv("BOT_TOKEN"),
    "database_url": os.getenv("DATABASE_URL")
}
