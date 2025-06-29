import numpy as np
import joblib
import pandas as pd

# 1. Load the trained model
try:
    clf = joblib.load("failure_classifier.pkl")
    print("✅ Model loaded successfully.")
except FileNotFoundError:
    print("❌ Model file 'failure_classifier.pkl' not found. Run classify_failure.py first.")
    exit()

# 2. Create a sample input
# Make sure this matches the number & order of features used in training
# You can also load from CSV if needed
# Format: [timestamp, power_consumption, voltage_levels, current_fluctuations, temperature, environmental_conditions, current_fluctuations_env]

sample_input = np.array([[int(pd.Timestamp("2025-06-13 22:30").value),   # timestamp (converted to int)
                          140.0,  # power_consumption (Watts)
                          220.0,  # voltage_levels (Volts)
                          1.4,    # current_fluctuations (Amperes)
                          37.0,   # temperature (Celsius)
                          2,      # environmental_conditions (encoded: e.g., 2 = cloudy, 1 = rainy, etc.)
                          0.6]])  # current_fluctuations_env (Amperes)

# 3. Predict failure
prediction = clf.predict(sample_input)[0]

# 4. Print result
if prediction == 1:
    print("⚠️ ALERT: This street light is likely to FAIL soon!")
    # Optional: send_sms_or_email_alert()
else:
    print("✅ Street light is working fine.")

