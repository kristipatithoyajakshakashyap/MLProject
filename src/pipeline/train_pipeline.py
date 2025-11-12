import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        pass

    def train(self):
        data=DataIngestion()
        train_data,test_data=data.initiate_data_ingestion()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_path=train_data,
                                                                              test_path=test_data)
        modelTrainer=ModelTrainer()
        print(modelTrainer.initiate_model_trainer(train_array=train_arr,
                                                  test_array=test_arr))

if __name__=="__main__":
    trainer=TrainPipeline()
    trainer.train()