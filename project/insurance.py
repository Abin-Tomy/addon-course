import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r"datasets\insurance.csv")
print(df.head())
print(df.isnull().sum())

# Convert categorical to numeric (sex, smoker, region)
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['region'] = le.fit_transform(df['region'])

# Choose features for clustering (age, bmi, charges)
X = df[['age', 'bmi', 'charges']].values
print(X[:5])

# Elbow Method
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

sns.set()
plt.plot(range(1,11), wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# Apply KMeans with 5 clusters (you can adjust based on elbow result)
kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
Y = kmeans.fit_predict(X)
print(Y)

# Visualize clusters (only first 2 dimensions: age vs charges)
plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,2], s=100, c="blue", label="Cluster 1")
plt.scatter(X[Y==1,0], X[Y==1,2], s=100, c="green", label="Cluster 2")
plt.scatter(X[Y==2,0], X[Y==2,2], s=100, c="red", label="Cluster 3")
plt.scatter(X[Y==3,0], X[Y==3,2], s=100, c="cyan", label="Cluster 4")
plt.scatter(X[Y==4,0], X[Y==4,2], s=100, c="magenta", label="Cluster 5")

# Plot centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,2], 
            s=200, c="yellow", edgecolors="black", marker="X", label="Centroids")

plt.title("Insurance Customers Clusters")
plt.xlabel("Age")
plt.ylabel("Charges")
plt.legend()
plt.show()
