import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Load dataset
df = pd.read_csv("street_light_fault_data.csv")

# 2. Clean column names (remove spaces, newlines, etc.)
df.columns = df.columns.str.strip().str.replace('\n', '').str.replace('\r', '')

# 3. Show cleaned column names
print("📋 Cleaned Columns:", df.columns.tolist())

# 4. Check for 'fault_type' column
if "fault_type" not in df.columns:
    raise Exception("❌ 'fault_type' column not found in dataset. Please verify column names.")

# 5. Create 'Failure' column: 1 if fault_type is NOT 'None', else 0
df["Failure"] = df["fault_type"].apply(lambda x: 0 if str(x).lower().strip() == "none" else 1)

# 6. Drop unnecessary columns (like IDs and fault_type)
df.drop(columns=["bulb_number", "fault_type"], inplace=True, errors='ignore')

# 7. Convert datetime columns (like 'timestamp') to integer
datetime_keywords = ['date', 'time', 'timestamp']
for col in df.columns:
    if any(word in col.lower() for word in datetime_keywords):
        try:
            df[col] = pd.to_datetime(df[col])
            df[col] = df[col].astype('int64')
            print(f"✅ Converted datetime: {col}")
        except Exception as e:
            print(f"⚠️ Could not convert datetime column {col}: {e}")

# 8. Label encode categorical columns if any
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            print(f"✅ Encoded column: {col}")
        except:
            print(f"⚠️ Skipped column (encoding failed): {col}")

# 9. Separate features and target
if "Failure" not in df.columns:
    raise Exception("❌ 'Failure' column is missing after processing!")

X = df.drop("Failure", axis=1)
y = df["Failure"]

# 10. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 11. Train classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# 12. Save the trained model
joblib.dump(clf, "failure_classifier.pkl")
print("✅ Model trained and saved as failure_classifier.pkl")
