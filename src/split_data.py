# split the raw data
# save the data/processed folder 

import os
from re import split
import pandas as pd
from sklearn.model_selection import train_test_split
import argparse
import yaml
import logging

# configuring logging operations
logging.basicConfig(filename='loggs.log', level=logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(message)s')

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def split_and_saved_data(config_path):
    config = read_params(config_path)
    train_data_path=config["split_data"]["train_path"]
    test_data_path=config["split_data"]["test_path"]
    source_data_path=config["data_source"]["source"]
    split_ratio=config["split_data"]["text_size"]
    random_state=config["base"]["random_state"]

    df=pd.read_csv(source_data_path)
    df=df.drop(["_id","Unnamed: 0"],axis=1)
    train,test=train_test_split(
        df,
        test_size=split_ratio,
        random_state=random_state
        )
    train.to_csv(train_data_path,index=False)
    test.to_csv(test_data_path,index=False)
    logging.info('Data split was doned and saved')


if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)