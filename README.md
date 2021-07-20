# Customer Churn Predictor
It is a machine learning project that predicts whether the customer will churn or not.
## Project Overview
It is a Flask-based Web Application hosted on the AWS EC2 http://ec2-3-143-22-251.us-east-2.compute.amazonaws.com:8080/ instance that Predicts whether the customer will churn or not using Logistic Regression (F-score: 86%).
## Installation
This project is developed using python 3.7. If you are using any lower version of python then I recommend you to upgrade your python to the latest version by using pip command. Follow the steps below to run this project locally.
```
git clone https://github.com/reenasheoran/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction-main
pip install -r requirements.txt
python app.py
```
## Motivation
In MBA, I learned that the success of every business is directly/indirectly dependent upon the type and number of customers the company has. **Customer churn**, also known as customer attrition, occurs when customers stop doing business with a company. A high customer churn rate indicates that the company is losing its customers rapidly. This churn can be because of myriad reasons, and it is the company that needs to discover these reasons via patterns and trends present in customer data. All companies are interested in identifying segments of these customers because the price for acquiring a new customer is usually higher than retaining the old one. For example, if Netflix knows a segment of customers who are at risk of churning, the company could proactively engage them with special offers instead of simply losing them.
## Problem Statement
The goal of this project is to create a web app that could help the companies to accurately predict which customers are most likely to churn so that the company could proactively engage them with special offers and retain business with them.
## Data Collection
The dataset has been taken from kaggle https://www.kaggle.com/blastchar/telco-customer-churn. It contains the data about telco customers where each row represents a customer, each column contains customer’s attributes.<br><br>
The data set includes information about:<br>
1. Customers who left within the last month – the column is called Churn <br>
2. Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies<br>
3. Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges<br>
4. Demographic info about customers – gender, age range, and if they have partners and dependents<br>

Original data size was 7043 rows and 21 columns.
## Feature Engineering
1. Feature "TotalCharges" was of object datatype, I converted it to numerical. As a result of this operation, 11 values resulted into null that I dropped from the original data.<br>
2. The data contains the values "No internet service" and "No phone service". Both of these values were converted into "No" in the data.<br>
3. All the columns that are containing only 2 values "Yes" and "No" are converted to int, where 1 represents "Yes" and 0 represents "No".<br>
4. Similarly, gender column is also converted to int, where 1 represents "Male" and 0 represents "Female".<br>
5. The columns with multiple categories (InternetService, Contract, PaymentMethod) were converted to dummy variables.<br>

After data cleaning the size of data was 7032 rows and 28 columns.<br>
## EDA
I looked at the distributions of the data. Below are few highlights from EDA section.
![EDA1](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/eda.png)<br>
![EDA2](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/eda4.png)<br>
![EDA3](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/eda1.png)<br>
![EDA4](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/eda2.png)<br>
![EDA5](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/eda3.png)<br>
![EDA6](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/corr.png)<br>
## Data Balancing
The data was imbalanced as shown in figure below.<br>
![imb](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/imb.png)<br>
## Model Bulding
For building the model, I first splitted the data into train and test set in 80:20 ratio respectively. Then I tried following models: -<br>
1. Logistic Regression<br>
2. K Nearest Neighbors<br>
3. Support Vector Machine<br>
4. Random Forest<br>
5. Naive Bayes<br> 
## Models Evaluation and Performance Metrics
For evaluating the model I recorded accuracy, F-score(Churn), F-score(Not Churn). For making the final decision I considered F-score (Churn) metrics, as the data was imbalanced so rather than accuracy F-score should be considered.Further, our concern is for Churn class only, therefore, I considered F-score(churn) over F-score(Not Churn). Following is the performance table: - <br>
Model|accuracy|F-score(Churn)|F-score(Not Churn)
---|---|---|---
Logistic Regression|0.794598|0.86|0.61
K Nearest Neighbors|0.749822|0.83|0.55
Support Vector Machine|0.778962|0.85|0.57
Random Forest|0.776830|0.85|0.56
Naive Bayes|0.749112|0.80|0.65

Since Logistic Regression has the highest F-score(Churn). This model is finalized for production.
## Productionization and Deployment
At this step, I built a flask based web app that is hosted on AWS EC2 instance http://ec2-3-143-22-251.us-east-2.compute.amazonaws.com:8080/ . The API endpoint takes in a request with a list of values entered by the app user and returns the predicted price of the flight ticket.
## Screen Shots
![Home Page](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/1.png)<br>
![Fill Entries](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/2.png)<br>
![Prediction](https://github.com/reenasheoran/Customer_Churn_Prediction/blob/main/images/3.png)<br>


