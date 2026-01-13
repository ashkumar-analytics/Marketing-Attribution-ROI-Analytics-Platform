import pandas as pd

def load_marketing_data(path: str):
    df = pd.read_csv(path)
    df["conversion_rate"] = df["conversions"] / df["clicks"]
    df["roi"] = (df["revenue"] - df["cost"]) / df["cost"]
    return df
