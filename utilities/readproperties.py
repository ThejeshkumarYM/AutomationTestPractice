import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")

class read_config_ini:
    @staticmethod
    def get_application_url():
        url=config.get("commoninfo","baseurl")
        return url

    @staticmethod
    def get_user_email():
        email=config.get("commoninfo","xyz@gmail.com")
        return email

    @staticmethod
    def get_user_password():
        password=config.get("commoninfo","testing")
        return password


