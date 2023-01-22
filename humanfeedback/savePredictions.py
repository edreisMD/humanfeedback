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

# create a wraper that receives a class called LLMChain or LLM and adda functionality when the function predict is called
class CustomLLMChain(LLMChain):
    # override the predict function
    def predict(self, text):
        # get the predictions from the original function
        predictions = super().predict(text)
        # save the predictions in the database
        df = loadPredictions()
        df = df.append({'prediction': predictions}, ignore_index=True)
        df.to_csv('predictions.csv', index=False)
        # return the predictions
        return predictions