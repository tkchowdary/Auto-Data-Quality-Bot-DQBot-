import pandas as pd
import yaml
from checks.null_check import null_check

df = pd.read_csv("data/sample_dataset.csv")

with open("config/dq_config.yaml") as f:
    config = yaml.safe_load(f)

report = null_check(df, config['thresholds'])

print(report)
# Optionally: write to JSON, send to Slack
