import pandas as pd
from sklearn.impute import KNNImputer

data = pd.read_csv("C:\\Users\\abint\Desktop\\addon-course\datasets\MISSING_DATASET_HANDLING.csv", encoding='latin1') #Load the dataset

# data = data.drop(columns=["ADDRESSLINE2"]) #remove the column ADDRESSLINE2
# data = data.dropna(subset=["ORDERDATE", "PRODUCTLINE"]) #remove the values that are not filled in the columns ORDERDATE and PRODUCTLINE
# data["MSRP"] = data["MSRP"].fillna(data["MSRP"].median()) #fill the missing values in the column MSRP with the median of the column
# data["YEAR_ID"] = data["YEAR_ID"].fillna(data["YEAR_ID"].mode()[0]) #fill the missing values in the column YEAR_ID with the mode of the column
# data["STATUS"].fillna(data["STATUS"].mode()[0], inplace=True) #fill the missing values in the column STATUS with the mode of the column
# data["PHONE"].fillna("Unknown", inplace=True) #fill the missing values in the column PHONE with the string "Unknown"

imputer = KNNImputer(n_neighbors=5) 
data_imputed = pd.DataFrame(imputer.fit_transform(data.select_dtypes(include=[float, int])), columns=data.select_dtypes(include=[float, int]).columns)
print(data.isnull().sum())
