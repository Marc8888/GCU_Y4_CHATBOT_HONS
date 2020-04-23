import os
import json

class Utility:
    @staticmethod
    def LoadJsonFile(filePath):
        # Load a file then turn it into a json object
        configuration_json = None
        with open(filePath, 'r') as file:
            configuration_json = json.loads(file.read())
        return configuration_json

    @staticmethod
    def LoadFileString(filePath):
        # Load a file into a string
        text = None
        with open(filePath, 'r') as file:
            text = file.read()
        return text