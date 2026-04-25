import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "edunexo-dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root@localhost/edunexo"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
