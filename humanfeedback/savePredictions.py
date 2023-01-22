# It is a pandas dataframe now but it will be replaced with a SQL database
import pandas as pd

from langchain import LLMChain
import os

# create a decorator for langchain to save the predictions in the database (for now a pandas dataframe)
def savePredictionsDecorator(func):

    # get the current path on a variable currentPath
    currentPath = os.getcwd()
    # load the database if it exists, otherwise create a new one
    # check if the file exists on the current path
    if os.path.isfile(currentPath + '/predictions.csv'):
        # load the database
        df = pd.read_csv(currentPath + '/predictions.csv')
    else:
        # create a new database
        df = pd.DataFrame(columns=['prediction'])

    # define the wrapper
    def wrapper(*args, **kwargs):

        # get the current path on a variable currentPath
        currentPath = os.getcwd()
        # get the prediction
        prediction = func(*args, **kwargs)
        # add the prediction to the database
        df = df.append({'prediction': prediction}, ignore_index=True)
        # save the database on the current path
        df.to_csv(currentPath + '/predictions.csv', index=False)
        # print save predictions 
        print('Saving predictions')
        # return the prediction
        return prediction
    # return the wrapper
    return wrapper

# return LLM or LLMChain with the decorator
def savePredictions(model):
    if isinstance(model, LLMChain):
        model.predict = savePredictionsDecorator(model.predict)

    return model
    
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
