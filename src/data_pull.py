from os import remove
import pandas as pd
import yaml
import pymongo
import argparse
import logging

# configuring logging operations
logging.basicConfig(filename='Logs/loggs.log', level=logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(message)s')

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def data_pull(config_path):
    config = read_params(config_path)
    data_path = config["data_fetch"]["data_pull"]
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['mushrooms_prediction']
    mycollection = db["mushrooms"]
    records = mycollection.find()
    dataframe = pd.DataFrame(records)
    dataframe.to_csv(data_path)

    logging.info('Data was collecter from mongodb ')

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data_pull(config_path=parsed_args.config)
