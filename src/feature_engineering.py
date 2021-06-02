import os
import argparse
from get_data import read_params
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def feature_eng(config_path):
    config= read_params(config_path)
    data_path=config["load_data"]["raw_data_csv"]
    df= pd.read_csv(data_path,sep=',',encoding='utf-8')
    
    # TotalCharges is object datatype, covert it to numerical
    pd.to_numeric(df.TotalCharges,errors='coerce').isnull().sum()
    df1= df[df.TotalCharges!= " "]
    df2=df1.copy()
    df2.loc[:,'TotalCharges']=pd.to_numeric(df2.TotalCharges)
    df3=df2.copy()
    df3.replace('No internet service', 'No', inplace=True)
    df4=df3.copy()
    df4.replace('No phone service','No', inplace=True)
    yesno_cols = ['Partner','Dependents','PhoneService','MultipleLines','OnlineSecurity','OnlineBackup','DeviceProtection',
              'TechSupport','StreamingTV','StreamingMovies','PaperlessBilling','Churn']
    df5=df4.copy()
    for col in yesno_cols:
        df5[col].replace({'Yes':1,'No':0},inplace=True)
    df5.gender.replace({'Male':1,'Female':0},inplace=True)

    dfnew = pd.get_dummies(data=df5,columns=['InternetService','Contract','PaymentMethod'])

    scale_cols= ['tenure','MonthlyCharges','TotalCharges']
    MM=MinMaxScaler()
    dfnew[scale_cols] = np.round(MM.fit_transform(dfnew[scale_cols]),4)
    filter_data_path=config["filter_data"]["filter_data_csv"]
    dfnew.to_csv(filter_data_path,sep=',',encoding='utf-8',header=True,index=False)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parsed_args=args.parse_args()
    feature_eng(config_path=Parsed_args.config)