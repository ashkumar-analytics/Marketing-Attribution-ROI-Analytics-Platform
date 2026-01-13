def channel_roi(df):
    return df.groupby("channel")[["revenue", "cost", "roi"]].mean().reset_index()
