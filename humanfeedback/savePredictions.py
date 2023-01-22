# It is a pandas dataframe now but it will be replaced with a SQL database
import pandas as pd
import os

# import llm chain
from langchain import LLMChain

# functions to load the predictions from the database
def loadPredictions():
    # load the database if it exists, otherwise create a new one
    # check if the file exists
    if os.path.isfile('predictions.csv'):
        # load the database
        df = pd.read_csv('predictions.csv')
    else:
        # create a new database
        df = pd.DataFrame(columns=['prediction'])
    # return the database
    return df

def savePrediction(prediction):
    # load the database
    df = loadPredictions()
    # add the prediction to the database
    df = df.append({'prediction': prediction}, ignore_index=True)
    # save the database
    df.to_csv('predictions.csv', index=False)

# create a wraper that receives a class called LLMChain or LLM and adda functionality when the function predict is called
class CustomLLMChain(LLMChain):
    # create a new constructor
    def __init__(self, *args, **kwargs):
        # call the original constructor
        super().__init__(*args, **kwargs)
        # save the original predict function
        self.original_predict = self.predict

    # create a new predict function
    def predict(self, *args, **kwargs):
        # call the original predict function
        prediction = self.original_predict(*args, **kwargs)
        # save the prediction to the database
        savePrediction(prediction)
        # return the prediction
        return prediction