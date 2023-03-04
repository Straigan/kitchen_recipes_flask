import os

from dotenv import load_dotenv


load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ['SECRET_KEY']
UPLOAD_PATH = os.path.join(basedir, 'static', 'media')
ALLOWED_IMAGE = set(['png', 'jpg', 'jpeg'])
MEDIA_FOLDER = 'media'
MAIL_SERVER = os.environ['MAIL_SERVER']
MAIL_PORT = os.environ['MAIL_PORT']
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
CELERY_BROKER_URL = 'redis://localhost:32701/0'
CELERY_RESULT_BACKEND = 'redis://localhost:32701/0'
