# It is a pandas dataframe now but it will be replaced with a SQL database
import pandas as pd

from langchain import LLMChain
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
class Wrapper(object):
    def __init__(self,wrapped_class):
        self.wrapped_class = wrapped_class()

    def __getattr__(self,attr):
        orig_attr = self.wrapped_class.__getattribute__(attr)
        if callable(orig_attr):
            def hooked(*args, **kwargs):
                self.pre()
                result = orig_attr(*args, **kwargs)
                # prevent wrapped_class from becoming unwrapped
                if result == self.wrapped_class:
                    return self
                self.post()
                return result
            return hooked
        else:
            return orig_attr

    def pre(self):
        # load the database
        self.df = loadPredictions()

    def post(self):
        # save the database
        self.df.to_csv('predictions.csv',index=False)