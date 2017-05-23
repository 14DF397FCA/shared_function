from configparser import ConfigParser


class IniFiles:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = None
        self.open_config()

    def open_config(self):
        self.config = ConfigParser()
        self.config.read(self.config_file)

    def read_option(self, section, option):
        return self.config[section][option]

    def write_option(self, section, option, value):
        self.config[section][option] = value
        with open(self.config_file, "w") as conf_file:
            self.config.write(conf_file)
