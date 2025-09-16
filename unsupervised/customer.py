import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv(r"datasets\Mall_Customers.csv", encoding="latin1")
print(df.isnull().sum())


X = df.iloc[:,[3,4]].values
print(X)

wcss=[]
for i in range(1,11):
    kmeans= KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)