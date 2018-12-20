import configparser
import os


class PyAxonautConfig:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config = configparser.ConfigParser()
        config.read(f'{dir_path}/config.ini')
        self.config = config

    def get_api_key(self):
        return self.config['CREDENTIALS']['API_KEY']
