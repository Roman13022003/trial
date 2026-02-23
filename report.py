from data import load_data2
from analysis import total_sales_by_city2

df = load_data2()
result = total_sales_by_city2(df)
print("Загальні продажі по містах2:")
print(result)

from analysis import average_sales_by_city

avg = average_sales_by_city(df)
print("\nСередні продажі по містах:")
print(avg)

