
def average_sales_by_city(df): return df.groupby("city")["sales"].mean()
def total_sales_by_city2(df):
    return df.groupby("city")["sales"].sum().sort_values(ascending=False)
