# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    SECRET_KEY = "ZhodZV8jwi_Oj00_5K7t9w"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://MSPROJ2021:rach_2021@localhost:3306/user_dev'
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    pass