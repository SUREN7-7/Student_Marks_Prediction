import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
#It is used to create lightweight, immutable-like, structured objects without writing boilerplate code.
#It automatically genetates __init__(),__repr__(),__eq__()

@dataclass  #decorator 
class DataIngestionConfig:
    #input path is given to this
    #artifacts is a folder used to see the output(train data)
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_congif=DataIngestionConfig()
        # So now ingestion_congif contains three paths

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            #we can extract data from any domain
            df=pd.read_csv(r'notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_congif.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_congif.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated.")
            train_set, test_set=train_test_split(df,test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_congif.train_data_path, index=False, header=True)
    
            test_set.to_csv(self.ingestion_congif.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed.")

            return (
                self.ingestion_congif.train_data_path,
                self.ingestion_congif.test_data_path
                
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()