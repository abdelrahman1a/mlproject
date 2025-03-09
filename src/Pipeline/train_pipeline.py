import sys

from src.logger import logging
from src.exception import CustomException
from src.Components.data_ingestion import DataIngestion
from src.Components.data_transformation import DataTransformation
from src.Components.model_trainer import ModelTrainer


def train_pipeline():

    try:
        logging.info("Trainig Pipeline Started")
        # Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path ,test_data_path)

        # Model Training
        model_trainer = ModelTrainer()
        best_model_Score= model_trainer.initiate_model_trainer(train_arr ,test_arr)
        print('Best Model Score is:' , best_model_Score)
        logging.info("Trainig Pipeline is Completed")

    except Exception as e:
        raise CustomException(e , sys)
    

if __name__ == '__main__':
    train_pipeline()

