import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
import dill

def save_object(file_path, obj):
    # Used to store preprocessing pipelines, trained models, or feature transformations.
    try:
        dir_path = os.path.dirname(file_path)     # "artifacts"
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)              # obj -> preprocessor(pipeline obj), file_path -> proprocessor.pkl
    except Exception as e:
        raise CustomException(e,sys)