"""SAS821S Lab 1 starter analysis script.
Complete the TODO sections. This file intentionally contains no answers.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

DATA = Path("02_Data")

auth = pd.read_csv(DATA / "ot_authentication_logs.csv", parse_dates=["timestamp"])
dns = pd.read_csv(DATA / "ot_dns_logs.csv", parse_dates=["timestamp"])
firewall = pd.read_csv(DATA / "ot_firewall_logs.csv", parse_dates=["timestamp"])
train = pd.read_csv(DATA / "ot_network_flow_training.csv", parse_dates=["timestamp"])
investigation = pd.read_csv(DATA / "ot_network_flow_investigation.csv", parse_dates=["timestamp"])

print("Authentication rows:", len(auth))
print("DNS rows:", len(dns))
print("Firewall rows:", len(firewall))

# TODO 1: data-quality checks (missing values, duplicates, data types).
# TODO 2: descriptive statistics and at least three visualisations.
# TODO 3: correlate the logs and construct an incident timeline.

FEATURES = [
    "dst_port", "duration_sec", "src_bytes", "dst_bytes", "packets",
    "connections_2s", "serror_rate", "rerror_rate", "same_srv_rate",
    "diff_srv_rate", "hour", "is_weekend"
]
X = train[FEATURES]
y = train["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=821, stratify=y
)

model = Pipeline([
    ("scale", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced")),
])
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, digits=3))

# TODO 4: score investigation flows and export the ten most suspicious rows.
investigation["predicted_malicious"] = model.predict(investigation[FEATURES])
investigation["malicious_probability"] = model.predict_proba(investigation[FEATURES])[:, 1]
# investigation.sort_values("malicious_probability", ascending=False).head(10).to_csv(
#     "top_10_suspicious_flows.csv", index=False
# )
