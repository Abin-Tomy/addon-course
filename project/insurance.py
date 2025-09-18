import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load dataset
df = pd.read_csv(r"datasets\insurance.csv")
print("Dataset Loaded Successfully\n")

# Encode categorical features
le = LabelEncoder()
for col in ['sex', 'smoker', 'region']:
    df[col] = le.fit_transform(df[col])

# Features & target
X = df.drop("charges", axis=1)
y = df["charges"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
accuracy = r2 * 100

print("Model Evaluation:")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")
print(f"Model Accuracy: {accuracy:.2f}%")

# Plot Actual vs Predicted
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Medical Insurance Charges")
plt.show()

# =============================
# User Input for Prediction
# =============================
print("\n=== Medical Insurance Cost Prediction ===")
age = int(input("Enter Age: "))
sex_val = 1 if input("Enter Sex (male/female): ").lower() == "male" else 0
bmi = float(input("Enter BMI: "))
children = int(input("Enter Number of Children: "))
smoker_val = 1 if input("Are you a Smoker? (yes/no): ").lower() == "yes" else 0
region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region_val = region_map.get(input("Enter Region (northeast/northwest/southeast/southwest): ").lower(), 0)

# Create input DataFrame
user_data = pd.DataFrame([[age, sex_val, bmi, children, smoker_val, region_val]], columns=X.columns)

# Predict
predicted_cost = model.predict(user_data)[0]
print(f"\nPredicted Medical Insurance Cost: ${predicted_cost:.2f}")
