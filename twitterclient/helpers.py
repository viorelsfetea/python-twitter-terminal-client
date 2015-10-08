import os
import ConfigParser


class Config(object):
    general_config_file = os.path.join(os.path.dirname(__file__), 'config')
    user_config_file = os.path.join(os.path.dirname(__file__), '.user_config')

    def load(self, type):

        config = ConfigParser.RawConfigParser()
        config.read(self.get_file_to_load(type))

        return config

    def get_file_to_load(self, type):
        files = {
            'general': self.general_config_file,
            'user': self.user_config_file,
        }

        return files[type]
    def save(self, data, key):
        config = ConfigParser.RawConfigParser()

        config.add_section(key)

        for item_key, item_value in data.iteritems():
            config.set(key, item_key, item_value)

        with open(self.user_config_file, 'wb') as configfile:
            config.write(configfile)
