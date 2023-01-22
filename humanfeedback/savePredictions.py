# It is a pandas dataframe now but it will be replaced with a SQL database
import pandas as pd
import os

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
class LLMChain:
    def __init__(self, llm):
        self.llm = llm
        self.predictions = loadPredictions()
        self.predictions = self.predictions.append({'prediction': 'test'}, ignore_index=True)
        self.predictions.to_csv('predictions.csv', index=False)

    def predict(self, input):
        # call the predict function of the LLM
        prediction = self.llm.predict(input)
        # save the prediction
        self.predictions = self.predictions.append({'prediction': prediction}, ignore_index=True)
        self.predictions.to_csv('predictions.csv', index=False)
        # return the prediction
        return prediction