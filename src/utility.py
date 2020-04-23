import os
import json

class Utility:
    @staticmethod
    def LoadJsonFile(filePath):
        configuration_json = None
        with open(filePath, 'r') as file:
            configuration_json = json.loads(file.read())
        return configuration_json

    @staticmethod
    def LoadFileString(filePath):
        text = None
        with open(filePath, 'r') as file:
            text = file.read()
        return text