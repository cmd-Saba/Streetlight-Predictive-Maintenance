Streetlight Predictive Maintenance using AI

This project is an AI-powered predictive maintenance system for smart streetlights. It uses Machine Learning models to:
- Detect if a streetlight is about to fail
- Predict remaining operational time (in hours)

Our aim is to ensure real-time monitoring, reduce downtime, and enhance public safety through automated alerts and actionable insights.

 Objectives
- Predict streetlight failure using classification models

- Estimate time to failure using regression

- Send automated email/SMS alerts on potential failures

- Enable officials to take proactive action

- Provide a clean and interactive web dashboard using HTML/CSS/JS



Dataset
Source: Kaggle Street Light Fault Prediction Dataset

Features include:
-Power consumption
-Voltage levels
-Temperature
-Environmental conditions
-Fault type

| Layer          | Technology                                                             |
| -------------- | ---------------------------------------------------------------------- |
|  Model       | `RandomForestClassifier`, `RandomForestRegressor` (via `scikit-learn`) |
|  Backend     | `Python`, `pandas`, `joblib`, `email/smtplib`                          |
|  Alerts      | `Email` (via Gmail SMTP)                                               |
|  Frontend | `HTML`, `CSS`, `JavaScript`                                               |
|  Hosting     | GitHub (collaborative repo)                                            |



