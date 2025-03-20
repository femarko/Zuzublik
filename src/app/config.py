import os
import pathlib

from dotenv import load_dotenv

load_dotenv(pathlib.Path(__file__).parents[2] / '.env')

config = {"bot_token": os.getenv("BOT_TOKEN")}
