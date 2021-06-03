from flask import Flask, render_template,request
import os
import numpy as np
import pandas as pd
import yaml
import joblib

webapp_root = "webapp"
params_path= "params.yaml"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__ , static_folder=static_dir,template_folder=template_dir)

def read_params(params_path):
    with open(params_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def LRpredict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    #prediction = model.predict(np.asarray(data).astype('float32'))
    prob = model.predict_proba(np.asarray(data).astype('float32'))
    Churnprob = prob[:,1]
    if Churnprob >= 0.25:
            response = 'Churn'
    else:
            response = 'Not churn'
    
    return response

@app.route('/', methods=['GET','POST'])
def home():
     if request.method == 'POST':
        Gender = request.form['Gender']
        if (Gender == 'Male'):
                    Gender = 1
        else:
                    Gender = 0
                    
        SeniorCitizen = request.form['SeniorCitizen']
        if (SeniorCitizen == 'Yes'):
                    SeniorCitizen = 1
        else:
                    SeniorCitizen = 0
                    
        Partner = request.form['Partner']
        if (Partner == 'Yes'):
                    Partner = 1
        else:
                    Partner = 0    
                    
        Dependents = request.form['Dependents']
        if (Dependents == 'Yes'):
                    Dependents = 1
        else:
                    Dependents = 0    
                    
        PhoneService = request.form['PhoneService']
        if (PhoneService == 'Yes'):
                    PhoneService = 1
        else:
                    PhoneService = 0    
                    
        MultipleLines = request.form['MultipleLines']
        if (MultipleLines == 'Yes'):
                    MultipleLines = 1
        else:
                    MultipleLines = 0   
                    
        InternetService = request.form['InternetService']
        if (InternetService == 'DSL'):
                    DSL = 1
                    Fibre_Optic = 0
                    No = 0
        elif (InternetService == 'Fibre Optic' ):
                    DSL = 0
                    Fibre_Optic = 1
                    No = 0   
        else:
                    DSL = 0
                    Fibre_Optic = 0
                    No = 1
        OnlineSecurity = request.form['OnlineSecurity']
        if (OnlineSecurity == 'Yes'):
                    OnlineSecurity = 1
        else:
                    OnlineSecurity = 0  
        OnlineBackup = request.form['OnlineBackup']
        if (OnlineBackup == 'Yes'):
                    OnlineBackup = 1
        else:
                    OnlineBackup = 0    
        DeviceProtection = request.form['DeviceProtection']
        if (DeviceProtection == 'Yes'):
                    DeviceProtection = 1
        else:
                    DeviceProtection = 0   
        TechSupport = request.form['TechSupport']
        if (TechSupport == 'Yes'):
                    TechSupport = 1
        else:
                    TechSupport = 0   
        StreamingTV = request.form['StreamingTV']
        if (StreamingTV == 'Yes'):
                    StreamingTV = 1
        else:
                    StreamingTV = 0   
        StreamingMovies = request.form['StreamingMovies']
        if (StreamingMovies == 'Yes'):
                    StreamingMovies = 1
        else:
                    StreamingMovies = 0  
        PaperlessBilling = request.form['PaperlessBilling']
        if (PaperlessBilling == 'Yes'):
                    PaperlessBilling = 1
        else:
                    PaperlessBilling = 0  
        Contract = request.form['Contract']
        if (Contract == 'Month-to-month'):
                    Month_to_month = 1
                    One_Year = 0
                    Two_Year = 0
        elif (Contract == 'One year'):
                    Month_to_month = 0
                    One_Year = 1        
                    Two_Year = 0  
        else:
                    Month_to_month = 0
                    One_Year = 0
                    Two_Year = 1
        PaymentMethod = request.form['PaymentMethod']
        if (PaymentMethod == 'Electronic check'):
                    Electronic_check = 1
                    Mailed_check = 0
                    Bank_transfer = 0
                    Credit_card = 0
        elif (PaymentMethod == 'Mailed check'):
                    Electronic_check = 0
                    Mailed_check = 1
                    Bank_transfer = 0
                    Credit_card = 0
        elif (PaymentMethod == 'Bank transfer (automatic)'):
                    Electronic_check = 0
                    Mailed_check = 0
                    Bank_transfer = 1
                    Credit_card = 0
        else:
                    Electronic_check = 0
                    Mailed_check = 0
                    Bank_transfer = 0
                    Credit_card = 1
        Tenure = request.form['Tenure']
        MonthlyCharges = request.form['MonthlyCharges']
        TotalCharges = request.form['TotalCharges']
        data = pd.DataFrame([{
               'gender': Gender,                                    
               'SeniorCitizen' : SeniorCitizen,                             
               'Partner' : Partner, 
               'Dependents' : Dependents,                               
               'tenure'   : Tenure,                                 
               'PhoneService' : PhoneService,                             
               'MultipleLines' : MultipleLines,
               'OnlineSecurity' : OnlineSecurity,                            
               'OnlineBackup'  : OnlineBackup,
               'DeviceProtection' : DeviceProtection ,                         
               'TechSupport'   : TechSupport,                            
               'StreamingTV'  : StreamingTV ,                             
               'StreamingMovies' : StreamingMovies ,                          
               'PaperlessBilling'  : PaperlessBilling,                        
               'MonthlyCharges'  : MonthlyCharges,                         
               'TotalCharges'  : TotalCharges,                                                              
               'InternetService_DSL' : DSL,                       
               'InternetService_Fiber optic'  : Fibre_Optic,             
               'InternetService_No'  : No,                      
               'Contract_Month-to-month' : Month_to_month,                   
               'Contract_One year'   : One_Year,                     
               'Contract_Two year'   : Two_Year,                      
               'PaymentMethod_Bank transfer (automatic)'   : Bank_transfer, 
               'PaymentMethod_Credit card (automatic)'   : Credit_card, 
               'PaymentMethod_Electronic check'       : Electronic_check,     
               'PaymentMethod_Mailed check': Mailed_check
                        }])
        
        response = LRpredict(data)
        print(response)
        
        return render_template('result.html', tables = [data.to_html(classes='data', header=True)],result = response)
     else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)












