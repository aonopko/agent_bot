import os

from dotenv import load_dotenv


load_dotenv()

DB_NAME = (os.getenv('DB_NAME'))
DB_PASSWORD = (os.getenv('DB_PASSWORD'))
DB_USER = (os.getenv('DB_USER'))
DB_HOST = (os.getenv('DB_HOST'))
POSTGRES_URI = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
