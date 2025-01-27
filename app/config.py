import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    GOOGLE_SHEET_ID = os.getenv('GOOGLE_SHEET_ID')
    GOOGLE_SHEET_GID = os.getenv('GOOGLE_SHEET_GID')
    GOOGLE_SHEET_URL = f'https://docs.google.com/spreadsheets/d/{GOOGLE_SHEET_ID}/export?format=csv&id={GOOGLE_SHEET_ID}&gid={GOOGLE_SHEET_GID}'