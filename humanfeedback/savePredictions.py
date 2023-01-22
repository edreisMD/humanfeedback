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
    # override predict function
    def predict(self, **kwargs: Any) -> str:
        """Format prompt with kwargs and pass to LLM.
        Args:
            **kwargs: Keys to pass to prompt template.
        Returns:
            Completion from LLM.
        Example:
            .. code-block:: python
                completion = llm.predict(adjective="funny")
        """
        # add new functionality
        # get the prediction
        prediction = self(kwargs)[self.output_key]
        # save the prediction
        savePrediction(prediction)
        # return the prediction
        return prediction