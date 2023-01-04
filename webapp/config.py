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