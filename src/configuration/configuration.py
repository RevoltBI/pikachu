import configparser
import os


class ConfigException(AttributeError):
    pass


class Config:
    def __init__(self, config: configparser.ConfigParser, section: str):
        self.__config = config
        self.__section = section
        # Fill in default values
        self.__config['DEFAULT'] = {
            'root_dir': '/opt/pikachu',
            'pin': 14,
            'interval': 0.5,
            'log_dir': '%(root_dir)s/logs',
            'debug': False,
            'log_format': '{"timestamp": "%%(asctime)s", "level": "%%(levelname)s", "filename":  "%%(filename)s", '
                          '"msg": "%%(message)s"}',
        }
        # Options that need to be set
        self.verify_attributes()

    def verify_attributes(self):
        attrs = ['root_dir']
        for attr in attrs:
            if not self.__config.has_option(self.__section, attr):
                raise ConfigException(f'Missing option: {attr}. '
                                      f'Fill the option to project root dir')

    @property
    def root_dir(self):
        return self.__config.get(self.__section, 'root_dir')

    @property
    def pin(self):
        return self.__config.getint(self.__section, 'pin')

    @property
    def interval(self):
        return self.__config.getfloat(self.__section, 'interval')

    @property
    def log_dir(self):
        return self.__config.get(self.__section, 'log_dir')

    @property
    def log_format(self):
        return self.__config.get(self.__section, 'log_format')

    @property
    def debug(self):
        return self.__config.getboolean(self.__section, 'debug')


def get_config(filename: str, section: str = "prod"):
    filename = os.path.abspath(filename)
    file_cfg = configparser.ConfigParser()
    file_cfg.read(filename)
    config = Config(file_cfg, section)
    return config
