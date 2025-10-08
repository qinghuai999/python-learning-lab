"""
File: ReadingConfigFiles.py
Author: Shiqi(Kiki) Su
Date: 2025-09-16 11:55
Description: How to read config and check if the config can normally work
"""

class UserData:
    """A class are using to check if it is correct."""

    def __init__(self):
        self.config = {}


    def read_config(self, filename: str) -> dict[str, dict[str, str]]:
        """
        Parse a configration file into a nested dictionary.

        The configuration file format:
            - Headings are enclosed in square bracket.
            - Each heading group together a set of key/value pairs.
            - Key/value pairs are written as 'name = value', one per line.
            - Lines outside a section heading are ignored.

        Args:
            filename (str): A name of the file that includes the path.

        Returns:
            dict[str, dict[str, str]]: Nested dictionary where each top-level
            key is a section name, and each value is a dictionary of key/value
            pairs that section.
        """
        pair = {}
        section = ''
        # Open file and get lines
        with (open(filename, 'r', encoding='utf-8') as file):
            for line in file:
                line = line.strip()
                # Process line's information to dictionary
                if not line or line.startswith('#') or line.startswith(';'):
                    continue

                if line.startswith('[') and line.endswith(']'):
                    if section and pair:
                        self.config[section] = pair
                        pair = {}
                    section = line.strip('[]')
                    continue
                if '=' in line:
                    if not section:
                        raise ValueError("This parameter doesn't have a heading.")
                    key, _, value = line.partition('=')
                    pair[key.strip()] = value.strip()
                    continue
                raise ValueError(f"Invalid config line: , {line!r}")
        self.config[section] = pair
        return self.config


    def get_value(self, setting_name: str) -> str:
        """
        Retrieve a nested value from the configration dictionary using
        a dot-seperated key.

        Args:
            config (dict[str, dict[str, str]]): The nested configuration
            dictionary returned by 'read_config'
            setting_name (str): A string in the form 'section.key'

        Returns:
            str: The value corresponding to the given dotted key.

        """
        # section, _, key = setting_name.partition('.')
        section, key = setting_name.split('.')
        pair = self.config[section]
        value = pair[key]
        return value


user = UserData()
print(user.read_config('week06_config.txt'))
print(user.get_value('notifications.sms'))