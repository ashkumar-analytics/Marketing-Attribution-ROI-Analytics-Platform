def last_touch_attribution(df):
    return df.groupby("channel")["revenue"].sum().reset_index()

def linear_attribution(df):
    total_channels = df["channel"].nunique()
    df["attributed_revenue"] = df["revenue"] / total_channels
    return df.groupby("channel")["attributed_revenue"].sum().reset_index()
