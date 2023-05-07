import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = True
    POSTGRES_URL = "pr3db.postgres.database.azure.com"
    POSTGRES_USER = "phucpa1@pr3db"
    POSTGRES_PW = "12345678abC"
    POSTGRES_DB = "techconfdb"
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL,
                                                          db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'q6cOjPkHc6fPmVahPkjjO1nwuxuHCsfVz+ASbAHaZ+I='
    SERVICE_BUS_CONNECTION_STRING = 'Endpoint=sb://phucpa1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=q6cOjPkHc6fPmVahPkjjO1nwuxuHCsfVz+ASbAHaZ+I='
    SERVICE_BUS_QUEUE_NAME = 'notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = ''  # Configuration not required, required SendGrid Account


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False