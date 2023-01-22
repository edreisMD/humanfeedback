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

# create a wraper for langchain LLMChain class to save the predictions in the database (for now a pandas dataframe in the working directory)
class Wraper(LLMChainClass):
    def __init__(self, *args, **kwargs):
        # call the init function of the LLMChainClass
        super(Wraper, self).__init__(*args, **kwargs)
        # load the predictions
        self.predictions = loadPredictions()
        # get the index of the last prediction
        self.index = len(self.predictions)
    def predict(self, *args, **kwargs):
        # call the predict function of the LLMChainClass
        prediction = super(Wraper, self).predict(*args, **kwargs)
        # save the prediction in the database
        self.predictions.loc[self.index] = prediction
        # increase the index
        self.index += 1
        # return the prediction
        return prediction