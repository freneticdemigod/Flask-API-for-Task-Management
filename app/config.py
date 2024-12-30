from dotenv import load_dotenv
import os

load_dotenv()

# database_url = os.getenv('SQLALCHEMY_DATABASE_URI')
database_url = 'postgresql://postgres:sahilR%4005@localhost:5432/task_management'
class Config:
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
