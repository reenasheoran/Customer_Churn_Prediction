import os
import argparse
import warnings
import sys
from get_data import read_params
import joblib
import json
import pandas as pd
from imblearn.combine import SMOTEENN
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import numpy as np


def evaluate_accuracy(actual, predicted):
    Accuracy_check = np.round(accuracy_score(actual, predicted), 4)
    Precision = np.round(precision_score(actual, predicted, average='weighted'),4)
    Recall = np.round(recall_score(actual, predicted, average='weighted'),4)
    F1_score = np.round(f1_score(actual, predicted, average='weighted'),4)

    return Accuracy_check, Precision, Recall, F1_score

def balance_data(X,Y):   
    SM = SMOTEENN()
    X_resampled, Y_resampled = SM.fit_resample(X,Y)
    return X_resampled, Y_resampled

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

    train_x_balanced, train_y_balanced = balance_data(train_x,train_y)
    test_x_balanced, test_y_balanced = balance_data(test_x,test_y)

    random_state = config["base"]["random_state"]
    n_estimators = config["estimators"]["RandomForest"]["Params"]["n_estimators"]
    criterion = config["estimators"]["RandomForest"]["Params"]["criterion"]
    min_samples_split = config["estimators"]["RandomForest"]["Params"]["min_samples_split"]
    
    RF = RandomForestClassifier(n_estimators=n_estimators,criterion=criterion,min_samples_split=min_samples_split,random_state=random_state)
    RF.fit(train_x_balanced, train_y_balanced)
    RFPrediction = RF.predict(test_x_balanced)

    (accuracy, Precision, Recall, F1_score) = evaluate_accuracy(test_y_balanced, RFPrediction)
    print("Model accuracy: %s" % accuracy)
    print("Model Precision: %s" % Precision)
    print("Model Recall: %s" % Recall)
    print("Model F1_score: %s" % F1_score)

    scores_file = config["report"]["scores"]
    with open(scores_file, 'w') as f:
        scores = {"acurracy": accuracy,
                    "f1_score": F1_score}
        json.dump(scores, f, indent=4)


    params_file = config["report"]["params"]
    with open(params_file, 'w') as f:
        params = {"n_estiamtors": n_estimators,
                  "criterion": criterion,
                  "min_samples_split": min_samples_split}
        json.dump(params, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(RF, model_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    args_parsed = args.parse_args()
    train_model(config_path=args_parsed.config)