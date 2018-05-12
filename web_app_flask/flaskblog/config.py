import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245' #move this env variable
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'#move this env variable
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
