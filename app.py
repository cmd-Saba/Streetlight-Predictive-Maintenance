from flask import Flask, request, jsonify
import pandas as pd
import joblib
from email_sms import send_email_alert

app = Flask(__name__)

# Load models
clf = joblib.load("failure_classifier.pkl")
reg = joblib.load("failure_regressor.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    df = pd.read_csv(file)

    df.columns = df.columns.str.strip()
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df['timestamp'] = df['timestamp'].astype('int64')

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = pd.factorize(df[col])[0]

    failure_preds = clf.predict(df)
    time_preds = reg.predict(df)

    df['Failure Prediction'] = ['FAIL' if i == 1 else 'OK' for i in failure_preds]
    df['Predicted Time to Failure (hrs)'] = time_preds.round(2)

    # Optional: email alert if any predicted failure
    if 1 in failure_preds:
        send_email_alert("Street light failure predicted.")

    result = df[['Failure Prediction', 'Predicted Time to Failure (hrs)']].to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
