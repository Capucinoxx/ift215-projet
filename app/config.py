import os

POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('SECRET_KEY')
