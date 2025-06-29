import streamlit as st
import pandas as pd
import joblib
from email_sms import send_email_alert  # Your existing file

st.set_page_config(page_title="Sunabeda Maintenance", layout="centered")
st.title("Street Light Predictive Maintenance 🔧")

# Load models
try:
    clf = joblib.load("failure_classifier.pkl")
    reg = joblib.load("failure_regressor.pkl")
    st.success("Models loaded successfully!")
except:
    st.error("❌ Could not load models. Make sure .pkl files exist.")
    st.stop()

# File upload
uploaded_file = st.file_uploader("Upload test CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        # Clean and preprocess
        df.columns = df.columns.str.strip()
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            df['timestamp'] = df['timestamp'].astype('int64')

        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = pd.factorize(df[col])[0]

        st.subheader("Uploaded Data")
        st.dataframe(df)

        # Prediction
        if st.button("Predict"):
            with st.spinner("Predicting..."):
                failure_preds = clf.predict(df)
                time_preds = reg.predict(df)

                result = df.copy()
                result["Failure Prediction"] = ["FAIL" if val == 1 else "OK" for val in failure_preds]
                result["Time to Failure (hrs)"] = time_preds.round(2)

                st.success("Prediction completed!")
                st.dataframe(result)

                if 1 in failure_preds:
                    try:
                        send_email_alert("⚠️ A street light is predicted to fail soon.")
                        st.info("Email alert sent.")
                    except Exception as e:
                        st.warning(f"Email failed: {e}")
    except Exception as e:
        st.error(f"Error processing file: {e}")


