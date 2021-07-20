# Customer Churn Predictor
It is a machine learning project that predicts whether the customer will churn or not.
## Project Overview
It is a Flask-based Web Application hosted on the AWS EC2 platform that Predicts whether the customer will churn or not using Logistic Regression (MAE ~ INR 1116.12).
## Installation
This project is developed using python 3.7. If you are using any lower version of python then I recommend you to upgrade your python to the latest version by using pip command. Follow the steps below to run this project locally.
```
git clone https://github.com/reenasheoran/Customer_Chirn_Prediction.git
cd Customer_Churn_Prediction-main
pip install -r requirements.txt
python app.py
```
## Motivation
In MBA, I learned that the success of every business is directly/indirectly dependent upon the type and number of customers the company has. **Customer churn**, also known as customer attrition, occurs when customers stop doing business with a company. A high customer churn rate indicates that the company is losing its customers rapidly. This churn can be because of myriad reasons, and it is the company that needs to discover these reasons via patterns and trends present in customer data. 
All companies are interested in identifying segments of these customers because the price for acquiring a new customer is usually higher than retaining the old one. For example, if Netflix knows a segment of customers who are at risk of churning, the company could proactively engage them with special offers instead of simply losing them.
## Problem Statement
The goal of this project is to create a web app that could help the companies to accurately predict which customers are most likely to churn so that the company could proactively engage them with special offers and retain business with them.
## Demo



## Data Collection
The dataset has been taken from kaggle https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh?select=Data_Train.xlsx. It contains the data about prices of flight tickets for various airlines and between various cities for the period between the months of March and June of 2019. Here is the details about data:-

Size of training set: 10683 records<br>
Size of test set: 2671 records

**FEATURES**: <br>
Airline: The name of the airline.<br>
Date_of_Journey: The date of the journey.<br>
Source: The source from which the service begins.<br>
Destination: The destination where the service ends.<br>
Route: The route taken by the flight to reach the destination.<br>
Dep_Time: The time when the journey starts from the source.<br>
Arrival_Time: Time of arrival at the destination.<br>
Duration: Total duration of the flight.<br>
Total_Stops: Total stops between the source and destination.<br>
Additional_Info: Additional information about the flight.<br>
Price: The price of the ticket.<br>
## Data Cleaning
Fortunately, there were only 2 missing values that too in the same row. Therefore, I dropped the row with NA values. 
## Feature Engineering
Then, I did feature engineering as follows: - <br>
-Converted column 'Date_of_Journey' from categorical to datetime dtype. Since all data is from same year, I am just extracted day and month from "Date_of_journey"<br>
-Extracted hours and minutes form "Dep_Time" <br>
-Extracted hour and minute from "Arrival_Time" <br>
-Extracted hour and minute from "Duration"<br>
-Applied one-hot encoding on categorical data such as total_stops, airline, source and destination features.<br>
## EDA
I looked at the distributions of the data and the prices of various airlines based on stoppages, source, destination, etc. Below are few highlights from EDA section.
![EDA1](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/4.png)
![EDA2](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/5.png)
![EDA3](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/6.png)
## Model Building
For building the model, I first splitted the data into train and test set in 80:20 ratio respectively. Then I tried following models: -<br>

## Models Evaluation and Performance Metrics
For evaluating the model I recorded Prediction R2 Score, Mean Absolute Error(MAE), Root Mean Squared Error(RMSE). For making the final decision I considered two metrics, Prediction R2 Score and Mean Absolute Error as these two metrics shows how good the model is on unknown data. Following is the performance table: - <br>
Model|R2 Score(Prediction)|MAE|RMSE
---|---|---|---
Linear Regression|0.6|1995.507|2936.755
Ridge Regression|0.599|2001.359|2942.245
Lasso Regression|0.599|1997.585|2939.402
ExtraTrees Regressor|0.806|1225.559|2047.61
RandomForest Regressor|0.794|1182.154|2109.848
LightGBM Regressor|0.823|1247.141|1955.4
XGBoost Regressor|0.844|1140.601|1834.37
CatBoost Regressor|0.865|1116.122|1704.965

Since CatBoost Regressor has the highest R2 score with minimum MAE score. This model is finalized for production.
## Productionization and Deployment
At this step, I built a flask based web app that is hosted on heroku platform https://flight-fare-predictor-mlop.herokuapp.com/ . The API endpoint takes in a request with a list of values entered by the app user and returns the predicted price of the flight ticket.
## Screen Shots
![Home Page](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/1.png)
![Fill Entries](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/2.png)
![Prediction](https://github.com/reenasheoran/Flight_Fare_MLOP/blob/main/static/3.png)


