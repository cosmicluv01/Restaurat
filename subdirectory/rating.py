import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Zomato Restaurant dataset.csv')
print(df.head())

# Exclude restaurants without a rating.
rated = df[df["Aggregate rating"] > 0]

#rating 
# Average rating
print("Average rating:", rated["Aggregate rating"].mean().round(2))

# Rating text  count (Excellent, Good, Average...)
print(df["Rating text"].value_counts())

# Rating  distribution
sns.histplot(rated["Aggregate rating"], bins=20, kde=True)
plt.title("Rating Distribution")
plt.show()

# City-wise average rating (kam se kam 20 restaurants wali cities)
city = rated.groupby("City")["Aggregate rating"].agg(["mean", "count"])
print(city[city["count"] >= 20].sort_values("mean", ascending=False).head(10))

# Online delivery / Table booking ka rating par asar
print(rated.groupby("Has Online delivery")["Aggregate rating"].mean())
print(rated.groupby("Has Table booking")["Aggregate rating"].mean())