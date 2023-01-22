# It is a pandas dataframe now but it will be replaced with a SQL database
import pandas as pd

# create a decorator for langchain to save the predictions in the database (for now a pandas dataframe)
def savePredictions(func):
    # load the database
    df = pd.read_csv('predictions.csv')
    # define the wrapper
    def wrapper(*args, **kwargs):
        # get the prediction
        prediction = func(*args, **kwargs)
        # add the prediction to the database
        df = df.append({'prediction': prediction}, ignore_index=True)
        # save the database
        df.to_csv('predictions.csv', index=False)
        # return the prediction
        return prediction
    # return the wrapper
    return wrapper
    
