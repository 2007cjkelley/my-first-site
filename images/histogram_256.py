import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("Assessor_-_Parcel_Sales_20251230.csv")
sale_price_num = (
    df["sale_price"]
      .astype(str)
      .str.replace(r"[\$,]", "", regex=True)
      .pipe(pd.to_numeric, errors="coerce")
)

print(sale_price_num.isna().sum())
print(sale_price_num.head(20))

#bins = pd.cut(sale_price_num, bins=8,include_lowest=True) print(bins.value_counts().sort_index())
# that instead of the section go to there!

edges = np.linspace(0, sale_price_num.max(), 256)
bins = pd.cut(sale_price_num, bins=edges, include_lowest=True)
#there!
# that gives a goofy bottom number equal to 1% of the max value, but the min value is 0
print(bins.value_counts().sort_index())

plt.hist(sale_price_num, bins=edges)
plt.xlabel("Sale price")
plt.ylabel("Number of sales")
plt.show()