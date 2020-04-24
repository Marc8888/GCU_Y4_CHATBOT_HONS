import os
import json
import threading

from deeppavlov import configs, build_model, train_model
from deeppavlov.core.common.file import read_json
from deeppavlov.core.common.chainer import Chainer
from utility import Utility

current_dir = os.path.dirname(os.path.realpath(__file__))
config_path = current_dir + "\\training_model.json"
config = Utility.LoadJsonFile(config_path)

class MLChatBot:
    # MLChatBot constructor
    def __init__(self):
        self.chatbotModel: Chainer = None
        self.bertModel: Chainer = None
        pass

# Train the model
def Train(self):
    self.chatbotModel = train_model(config, download=True)
    self.chatbotModel.save()

    # Load the bert database
    self.bertInsultsModel = build_model(configs.classifiers.insults_kaggle_bert, download=True)

    # Load the model
    def LoadModels(self):
        # Load the training model
        self.chatbotModel = build_model(config_path, download=True)

        # Load the bert insults database
        self.bertInsultsModel = build_model(configs.classifiers.insults_kaggle_bert, download=True)

    # Save any changes to the training model
    def Save(self):
        # If our model is loaded then save it
        if self.chatbotModel is not None:
            self.chatbotModel.save()
        pass

    # Get the training model
    def GetModel_Chat(self): # Get our chatbot
        return self.chatbotModel
    
    def GetModel_BertInsults(self): # Get our insults db
        return self.bertInsultsModel

    # Get the chatbot response
    def GetResponse(self, message):
        # Load the chatbot model if its not loaded
        if self.chatbotModel == None:
            self.LoadModel()

        insultCheck = self.bertInsultsModel([ message ])

        # Check if an insult was detected
        if (insultCheck[0] == "Insult"):
            # Return a default response
            return ["Im sorry I'm currently unable to answer that question (ERROR: Insult-Detected)", 0]
        else:
            # Run the training model
            return self.chatbotModel([ message ])