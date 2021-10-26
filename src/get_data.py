#read params
## process
## return dataframe

import os
import yaml
import pandas as pd
import argparse
import logging

# configuring logging operations
logging.basicConfig(filename='loggs.log', level=logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(message)s')

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["source"]
    df = pd.read_csv(data_path)
    return df
logging.info('data was read sucessfully') 

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)