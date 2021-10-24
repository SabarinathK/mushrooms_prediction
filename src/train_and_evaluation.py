# load the train and test
# train algorithm
# save the metrices, params

import os
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from urllib.parse import urlparse
from get_data import read_params
import argparse
import json
import joblib


def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path=config["encoder"]["train_path"]
    test_data_path=config["encoder"]["test_path"]
    model_path=config["model_dir"]
    random_state=config["base"]["random_state"]
    cache_size=config["estimator"]["SVC"]["params"]['cache_size']
    degree=config["estimator"]["SVC"]["params"]["degree"]
    target= config["base"]["target_col"]
    model_dir=config["model_dir"]


    train=pd.read_csv(train_data_path)
    test=pd.read_csv(test_data_path)

    y_train=train[target]
    y_test=test[target]

    X_train=train.drop(target, axis=1)
    X_test=test.drop(target, axis=1)


    model = SVC(
        cache_size=cache_size, 
        degree=degree, 
        random_state=random_state)
    model.fit(X_train, y_train)

    predicted_qualities = model.predict(X_test)

    report= classification_report(y_test, predicted_qualities)

    print("SVC model (cache_size=%f, degree=%f):" % (cache_size, degree))
    print("  metric: %s" % report)


#####################################################
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f:
        scores = {
            "metric": report
        }

        json.dump(scores,f)

    with open(params_file, "w") as f:
        params = {
            "cache_size": cache_size,
            "degree": degree,
        }
        json.dump(params,f)
#####################################################


    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(model, model_path)
    
if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)