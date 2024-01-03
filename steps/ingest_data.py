import logging
import pandas as pd

from zenml import step

class IngestData:
    """
    Ingesting the data
    """
    def __init__(self,data_path:str):
        """Instatiate the method"""
        self.data_path=data_path
    def get_data(self):
        """
        Get data from file
        Args:
            None
        Returns:
            Dataframe
        """
        data=pd.read_csv(self.data_path)
        return data
@step
def input_data(data_path:str)->pd.DataFrame:
    """"
    Ingesting the data  from data frame

    Args:
        data_path:path to the data

    Returns:
        pd.DataFrame the ingested data
    """
    try:
        ingestData=IngestData(data_path=data_path)
        data=ingestData.get_data()
        return data
    except Exception as e:
        logging.error("Error while ingesting the data")
        raise e
    