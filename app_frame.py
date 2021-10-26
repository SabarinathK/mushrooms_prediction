import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import joblib
params_path="params.yaml"
webapp_model_dir ="webapp_model_dir"
import yaml



class app_frame:
    def __init__(self) -> None:
        pass
    
    def read_params(config_path):
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
        return config

    def data_clean(df):
        encoder = LabelEncoder()
        for column in range(len(df.columns)):
            df[df.columns[column]]= encoder.fit_transform(df[df.columns[column]])
        return df
            