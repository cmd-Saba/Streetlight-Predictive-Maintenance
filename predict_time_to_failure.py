import pandas as pd
import random
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Load dataset
df = pd.read_csv("street_light_fault_data.csv")

# 2. Smart datetime conversion (only if column name hints it)
datetime_keywords = ['time', 'date', 'timestamp']
for col in df.columns:
    if any(kw in col.lower() for kw in datetime_keywords):
        try:
            df[col] = pd.to_datetime(df[col])
            df[col] = df[col].astype('int64')
            print(f"✅ Converted datetime column: {col}")
        except:
            print(f"⚠️ Failed to convert datetime column: {col}")

# 3. Encode categorical columns
for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        try:
            df[col] = le.fit_transform(df[col])
            print(f"✅ Encoded categorical column: {col}")
        except:
            print(f"⚠️ Skipping column: {col}")

# 4. Add dummy TimeToFailure target column
df["TimeToFailure"] = [random.randint(10, 1000) for _ in range(len(df))]

# 5. Prepare training data
X = df.drop(columns=["TimeToFailure"])
y = df["TimeToFailure"]

# 6. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 7. Model training
model = RandomForestRegressor()
model.fit(X_train, y_train)

# 8. Evaluation
preds = model.predict(X_test)
print("✅ MSE:", mean_squared_error(y_test, preds))

# 9. Save the model
joblib.dump(model, "time_regressor.pkl")
print("✅ Model saved as time_regressor.pkl")

