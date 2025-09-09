import pandas as pd

data = pd.read_csv("C:\\Users\\abint\Desktop\\addon-course\datasets\MISSING_DATASET_HANDLING.csv", encoding='latin1') #Load the dataset

data = data.drop(columns=["ADDRESSLINE2"]) #remove the column ADDRESSLINE2
data = data.dropna(subset=["ORDERDATE", "PRODUCTLINE"]) #remove the values that are not filled in the columns ORDERDATE and PRODUCTLINE
data["MSRP"] = data["MSRP"].fillna(data["MSRP"].median()) #fill the missing values in the column MSRP with the median of the column
data["YEAR_ID"] = data["YEAR_ID"].fillna(data["YEAR_ID"].mode()[0]) #fill the missing values in the column YEAR_ID with the mode of the column
print(data.isnull().sum())
