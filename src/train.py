import os
import json
from deeppavlov import configs, build_model, train_model
from deeppavlov.core.common.file import read_json
from ml import MLChatBot

# Create the chatbot
# Train it and Save
chatbot = MLChatBot()
chatbot.Train()
chatbot.Save()

# Interactive
while True:
    print("Enter question> ", end='')
    user_input = input()

    if user_input == 'exit':
        exit(1)

    response = chatbot.GetResponse(user_input)
    print(response[0])