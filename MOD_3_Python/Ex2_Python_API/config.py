import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = r"sqlite:///C:\Users\swain\db\mydb.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

