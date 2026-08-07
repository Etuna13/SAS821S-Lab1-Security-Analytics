# SAS821S Security Analytics Lab 1
## Incident at Omumborombonga Telecom

This repository contains the reproducible analysis conducted for SAS821S Security Analytics Lab 1 at the Namibia University of Science and Technology.

The investigation examines suspicious weekend activity detected at Omumborombonga Telecom using authentication, DNS, firewall, asset, user-directory and network-flow evidence.

## Investigation Objective

The investigation aimed to determine whether a security incident occurred, identify the affected user and endpoint, reconstruct the sequence of events, evaluate a supervised machine-learning detection model, and recommend appropriate security actions.

## Key Findings

The investigation identified suspicious activity associated with:

- User account: `nshikongo`
- Endpoint: `WKST-FIN-023`
- Source IP: `10.14.7.23`
- Department: Finance
- External IP: `45.77.89.11`
- Associated domain: `cdn-sync-update.com`

The evidence showed off-hours access to critical internal systems, repeated failed remote authentication followed by successful access, rapid multi-service internal connections, significant data collection from internal systems, and approximately 426.69 MB of outbound traffic to the associated external infrastructure.

The overall incident assessment was made with high confidence based on correlation across multiple independent evidence sources.

## Security Analytics Workflow

The investigation followed the Security Analytics Process Lifecycle:

1. Frame analytical questions
2. Acquire and validate evidence
3. Prepare and enrich the datasets
4. Establish behavioural baselines
5. Detect anomalies
6. Correlate evidence across logs
7. Train and evaluate a supervised model
8. Score investigation network flows
9. Communicate findings and recommendations

## Machine-Learning Model

An interpretable Decision Tree classifier was trained using the following network-flow features:

- `connections_2s`
- `serror_rate`
- `rerror_rate`
- `same_srv_rate`
- `diff_srv_rate`

A stratified 70/30 training-test split was used with a fixed random seed of 42.

### Test Results

| Metric | Result |
|---|---:|
| Accuracy | 88.61% |
| Precision | 62.21% |
| Recall | 100.00% |
| F1-score | 76.70% |
| False Negative Rate | 0.00% |

The model correctly identified all malicious flows in the labelled test set, although false positives remained an operational limitation.

## Repository Contents

- `SAS821S_Lab1_Investigation.ipynb` — complete reproducible Python investigation
- `outputs/top_10_suspicious_flows.csv` — required ranked model output
- `report/` — final incident report
- `software_requirements.txt` — supplied software requirements
- `.gitignore` — prevents raw evidence and temporary files from being published

## Evidence Handling

The original course-provided evidence is intentionally excluded from this repository.

Raw CSV evidence and reference hashes are stored locally in `data_raw/` and are not modified during analysis. Data preparation and investigation are performed using Python dataframes to preserve the integrity of the original evidence.

## Reproducibility

The analysis was successfully executed from top to bottom in a clean Jupyter kernel.

Environment used:

- Python 3.14.0
- pandas 3.0.5
- matplotlib 3.11.1
- scikit-learn 1.9.0

## Academic Context

This repository was produced as an individual practical assessment for:

**SAS821S — Security Analytics**  
**Semester 2, 2026**  
**Namibia University of Science and Technology**

