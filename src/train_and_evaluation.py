# load the train and test
# train algorithm
# save the metrices, params
import os
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import argparse
import json
import joblib
import yaml
import logging

# configuring logging operations
logging.basicConfig(filename='Logs/loggs.log', level=logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(message)s')

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path=config["encoder"]["train_path"]
    test_data_path=config["encoder"]["test_path"]
    random_state=config["base"]["random_state"]
    cache_size=config["estimator"]["SVC"]["params"]['cache_size']
    degree=config["estimator"]["SVC"]["params"]["degree"]
    target= config["base"]["target_col"]


    train=pd.read_csv(train_data_path)
    test=pd.read_csv(test_data_path)

    y_train=train[target]
    y_test=test[target]

    X_train=train.drop(target, axis=1)
    X_test=test.drop(target, axis=1)
    logging.info('features and label was selected ')

    model = SVC(
        cache_size=cache_size, 
        degree=degree, 
        random_state=random_state)
    model.fit(X_train, y_train)
    logging.info('model "SVC "selected and trained')

    predicted_qualities = model.predict(X_test)

    report= classification_report(y_test, predicted_qualities,zero_division=0)

#####################################################
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f:
        scores = {
            "metric": report
        }

        json.dump(scores,f)
    logging.info('metrics report was saved')


    with open(params_file, "w") as f:
        params = {
            "cache_size": cache_size,
            "degree": degree,
        }
        json.dump(params,f)
    logging.info('model parameter was saved')
#####################################################

    joblib.dump(model,open("models/model.pkl", 'wb'))
    logging.info('model,pkl "SVC " was done ')

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)