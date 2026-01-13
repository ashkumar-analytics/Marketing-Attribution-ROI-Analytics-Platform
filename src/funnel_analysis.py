def funnel_metrics(df):
    return {
        "total_impressions": df["impressions"].sum(),
        "total_clicks": df["clicks"].sum(),
        "total_conversions": df["conversions"].sum(),
        "overall_conversion_rate": df["conversions"].sum() / df["clicks"].sum()
    }
