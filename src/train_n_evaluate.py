import os
import argparse
import warnings
import sys

from sklearn.utils import class_weight
from get_data import read_params
import joblib
import json
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import numpy as np


def evaluate_accuracy(actual, predicted):
    Accuracy_check = np.round(accuracy_score(actual, predicted), 4)
    Precision = np.round(precision_score(actual, predicted, average='weighted'),4)
    Recall = np.round(recall_score(actual, predicted, average='weighted'),4)
    F1_score = np.round(f1_score(actual, predicted, average='weighted'),4)

    return Accuracy_check, Precision, Recall, F1_score


def train_model(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    model_dir = config["model_dir"]
    random_state = config["base"]["random_state"]
    target = config["base"]["target"]

    train = pd.read_csv(train_data_path, sep=',')
    test = pd.read_csv(test_data_path, sep=',')

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    train_y = train[target]
    test_y = test[target]


    random_state = config["base"]["random_state"]
    penalty = config["estimators"]["Logistic"]["Params"]["penalty"]
    class_weight = config["estimators"]["Logistic"]["Params"]["class_weight"]
    max_iter = config["estimators"]["Logistic"]["Params"]["max_iter"]
    
    LR=LogisticRegression(penalty=penalty,class_weight=class_weight,max_iter=max_iter,random_state=42)
    LRmodel=LR.fit(train_x,train_y)
    LRPrediction=LR.predict(test_x)

    (accuracy, Precision, Recall, F1_score) = evaluate_accuracy(test_y, LRPrediction)
    print("Model accuracy: %s" % accuracy)
    print("Model Precision: %s" % Precision)
    print("Model Recall: %s" % Recall)
    print("Model F1_score: %s" % F1_score)

    scores_file = config["report"]["scores"]
    with open(scores_file, 'w') as f:
        scores = {"acurracy": accuracy,
                    "Precision": Precision,
                    "Recall": Recall,
                    "f1_score": F1_score}
        json.dump(scores, f, indent=4)


    params_file = config["report"]["params"]
    with open(params_file, 'w') as f:
        params = {"max_iter": max_iter,
                  "penalty": penalty,
                  "class_weight": class_weight}
        json.dump(params, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(LR, model_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    args_parsed = args.parse_args()
    train_model(config_path=args_parsed.config)