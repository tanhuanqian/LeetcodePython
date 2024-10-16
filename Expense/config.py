import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://progres:1234@localhost/expense")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret")