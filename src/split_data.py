import os
import argparse
from get_data import read_params
import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(config_path):
    config = read_params(config_path)
    data_path = config["select_data"]["select_data_csv"]
    df = pd.read_csv(data_path,sep=',',encoding='utf-8')

    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    train,test=train_test_split(df,test_size=split_ratio,random_state=random_state)
    train_data_path=config["split_data"]["train_path"]
    test_data_path=config["split_data"]["test_path"]
    train.to_csv(train_data_path,sep=',',encoding='utf-8',index=False)
    test.to_csv(test_data_path,sep=',',encoding='utf-8',index=False)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parsed_args=args.parse_args()
    split_data(config_path=Parsed_args.config)