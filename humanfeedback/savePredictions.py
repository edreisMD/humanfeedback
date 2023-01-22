# It is a pandas dataframe now but it will be replaced with a SQL database
import pandas as pd

from langchain import LLMChain
import os

# create a wraper for langchain LLMChain class to save the predictions in the database (for now a pandas dataframe in the working directory)
class LLMChainWrapper(LLMChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # check if the file exists
        if os.path.isfile('predictions.csv'):
            # load the database
            self.df = loadPredictions()
        else:
            # create a new database
            self.df = pd.DataFrame(columns=['prediction'])
            # save the database
            self.df.to_csv('predictions.csv', index=False)

    def predict(self, *args, **kwargs):
        prediction = super().predict(*args, **kwargs)
        self.df = self.df.append({'prediction': prediction}, ignore_index=True)
        self.df.to_csv('predictions.csv', index=False)
        return prediction 

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
