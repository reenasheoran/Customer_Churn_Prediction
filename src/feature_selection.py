import os
import argparse
from get_data import read_params
import pandas as pd

def split_data(config_path):
    config = read_params(config_path)
    data_path = config["filter_data"]["filter_data_csv"]
    df = pd.read_csv(data_path,sep=',',encoding='utf-8')
    df = df.drop(['customerID'],axis=1)
    select_data_path=config["select_data"]["select_data_csv"]
    df.to_csv(select_data_path,sep=',',encoding='utf-8',header=True,index=False)


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parsed_args=args.parse_args()
    split_data(config_path=Parsed_args.config)