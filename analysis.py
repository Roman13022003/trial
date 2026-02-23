def total_sales_by_city2(df):
    return df.groupby("city")["sales"].sum()
