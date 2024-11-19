import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey') # Flask tomará la clave del .env en lugar de la predeterminada.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:KM1013599968@localhost:5432/DBCyberTest')