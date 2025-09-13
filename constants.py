from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

mysql_uri = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
