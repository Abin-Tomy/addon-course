import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
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

sns.set()
plt.plot(range(1,11), wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.show()

Clusters = 5
kmeans= KMeans(n_clusters=5, init="k-means++", random_state=42)
Y = kmeans.fit_predict(X)
print(Y)

Clusters =0,1,2,3,4
plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=100, c="blue", label="Cluster 1")
plt.scatter(X[Y==1,0], X[Y==1,1], s=100, c="green", label="Cluster 2")
plt.scatter(X[Y==2,0], X[Y==2,1], s=100, c="red", label="Cluster 3")
plt.scatter(X[Y==3,0], X[Y==3,1], s=100, c="cyan", label="Cluster 4")
plt.scatter(X[Y==4,0], X[Y==4,1], s=100, c="magenta", label="Cluster 5")

#centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c="red", label="Centroids")
plt.title("Customers Group")
plt.xlabel("Annual Income")
plt.show()