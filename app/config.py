from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('SQLALCHEMY_DATABASE_URI')
class Config:
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
