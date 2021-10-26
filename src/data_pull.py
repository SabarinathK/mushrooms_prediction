from os import remove
import pandas as pd
import yaml
import pymongo
import argparse

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

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data_pull(config_path=parsed_args.config)
