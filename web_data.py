import json
import os


class WebData:
    def __init__(self):
        """No init required"""

    @staticmethod
    def put(key, value):
        """
        Store a value against a key in the web data store
        """
        data = {}

        if os.path.isfile('./web_data.json'):
            with open("web_data.json", "r") as jsonFile:
                data = json.load(jsonFile)

        data[key] = value

        with open("web_data.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    @staticmethod
    def get(key):
        """
        Get a value for a key from the web data store
        """
        if os.path.isfile('./web_data.json'):
            f = open("web_data.json", "r")
            data = json.load(f)
            if key in data:
                return data[key]

        return ''
