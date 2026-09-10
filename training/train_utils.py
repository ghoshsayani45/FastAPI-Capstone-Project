'''
    This file contains the constants defined for
    writing the model traing script
'''

import os

DATA_DIR = 'data'   # directory where dataset file is stored
DATA_FILE_NAME = 'car-details.csv'      # name of the dataset file
DATA_FILE_PATH = os.path.join(DATA_DIR,DATA_FILE_NAME)  # complete path of the dataset file - /data/car-details.csv

APP_DIR = 'app'             
MODEL_DIR_NAME = 'models'
MODEL_NAME = 'model.joblib'                             # serialized model name
MODEL_DIR = os.path.join(APP_DIR,MODEL_DIR_NAME)        # directory where serialized model will be saved 
MODEL_PATH = os.path.join(MODEL_DIR,MODEL_NAME)         # complete path of the model file - /app/models/model.joblib