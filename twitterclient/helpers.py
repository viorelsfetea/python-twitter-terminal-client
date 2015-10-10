import os
import ConfigParser


class Config(object):
    general_config_file = os.path.join(os.path.dirname(__file__), 'config')
    user_config_file = os.path.join(os.path.dirname(__file__), '.user_config')

    def load(self, config_type):
        """
        Load the relevant config file based on its type
        :param config_type:
        :return:
        """
        config = ConfigParser.RawConfigParser()
        config.read(self.get_file_to_load(config_type))

        return config

    def save(self, data, key):
        """
        Save the user config info to the config file
        :param data:
        :param key:
        :return:
        """
        config = ConfigParser.RawConfigParser()

        config.add_section(key)

        for item_key, item_value in data.iteritems():
            config.set(key, item_key, item_value)

        with open(self.user_config_file, 'wb') as configfile:
            config.write(configfile)

    def get_file_to_load(self, config_type):
        """
        Get the config file name based on its type
        :param type:
        :return:
        """
        files = {
            'general': self.general_config_file,
            'user': self.user_config_file,
        }

        return files[config_type]