# GCU_Y4_CHATBOT_HONS

The chatbot source code can be found inside `/src`
The data that is being used as a source for the chatbot is inside `TestData.xlsx` which is converted to a CSV located inside `src/TestData.scv`

# Setup

Download the source code
Edit the `training_model.json`
Modify the `ROOT_PATH` variable and set it to the `src` folder location

## Run the trainer
```
python train.py
```

## Run the web server
- Make sure you train the model
```
python server.py
```