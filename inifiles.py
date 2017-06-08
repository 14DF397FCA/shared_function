"""
Version 1.0
"""
from configparser import ConfigParser


class IniFiles:
    """
    Simple class for work with INI files
    """
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = None
        self.open_config()

    def open_config(self):
        """
        Open configuration file
        :return: 
        """
        self.config = ConfigParser()
        self.config.read(self.config_file)

    def read_option(self, section, option):
        """
        Read value from configuration file
        :param section: 
        :param option: 
        :return: 
        """
        return self.config[section][option]

    def write_option(self, section, option, value):
        """
        Save value to configuration file
        :param section: 
        :param option: 
        :param value: 
        :return: 
        """
        self.config[section][option] = value
        with open(self.config_file, "w") as conf_file:
            self.config.write(conf_file)
