import pandas as pd
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]

df = pd.read_csv("sales/Zomato Restaurant Dataset (1).csv", encoding="latin-1")

print(df.head())
import pandas as pd

df = pd.read_csv("sales/Zomato Restaurant Dataset (1).csv", encoding="latin-1")

# 1. clean Column names 
df.columns = df.columns.str.strip()

# 2. clear Duplicates 
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# 3. find and write Missing values 
print(df.isna().sum())
df["Cuisines"] = df["Cuisines"].fillna("Unknown")

# 4. remove extra space from Text columns 
for col in ["Restaurant Name", "City", "Locality", "Cuisines"]:
    df[col] = df[col].astype(str).str.strip()

# 5. Yes/No columns  clean 
for col in ["Has Table booking", "Has Online delivery"]:
    df[col] = df[col].str.strip().str.title()

# 6. Numeric columns ke dtypes theek karo
df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce")
df["Aggregate rating"] = pd.to_numeric(df["Aggregate rating"], errors="coerce")
df["Average Cost for two"] = pd.to_numeric(df["Average Cost for two"], errors="coerce")

# 7. Galat values dhoondho
print("Rating 0 (not rated):", (df["Aggregate rating"] == 0).sum())
print("Cost 0:", (df["Average Cost for two"] == 0).sum())
print("Coordinates (0,0):", ((df["Latitude"] == 0) & (df["Longitude"] == 0)).sum())

# 8. Not-rated restaurants alag rakho (analysis ke liye)
rated = df[df["Aggregate rating"] > 0]

# 9. Outliers check (IQR method)
q1 = df["Average Cost for two"].quantile(0.25)
q3 = df["Average Cost for two"].quantile(0.75)
iqr = q3 - q1
outliers = df[(df["Average Cost for two"] < q1 - 1.5 * iqr) |
              (df["Average Cost for two"] > q3 + 1.5 * iqr)]
print("Cost outliers:", len(outliers))

# 10. Cleaned file save karo
df.to_csv("zomato_clean.csv", index=False, encoding="utf-8")
print("Final shape:", df.shape)

#rating analysis
# Average rating
print("Average rating:", rated["Aggregate rating"].mean().round(2))

# Rating text ka count (Excellent, Good, Average...)
print(df["Rating text"].value_counts())

# Rating ka distribution
plt.hist(rated["Aggregate rating"], bins=20, edgecolor="black")
plt.title("Rating Distribution")
plt.show()

# City-wise average rating (kam se kam 20 restaurants wali cities)
city = rated.groupby("City")["Aggregate rating"].agg(["mean", "count"])
print(city[city["count"] >= 20].sort_values("mean", ascending=False).head(10))

# Online delivery / Table booking ka rating par asar
print(rated.groupby("Has Online delivery")["Aggregate rating"].mean())
print(rated.groupby("Has Table booking")["Aggregate rating"].mean())

#RATING ANALYSIS
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

# Rating text ka count (Excellent, Good, Average...)
print(df["Rating text"].value_counts())

# Rating ka distribution
sns.histplot(rated["Aggregate rating"], bins=20, kde=True)
plt.title("Rating Distribution")
plt.show()

# City-wise average rating (kam se kam 20 restaurants wali cities)
city = rated.groupby("City")["Aggregate rating"].agg(["mean", "count"])
print(city[city["count"] >= 20].sort_values("mean", ascending=False).head(10))

# Online delivery / Table booking ka rating par asar
print(rated.groupby("Has Online delivery")["Aggregate rating"].mean())
print(rated.groupby("Has Table booking")["Aggregate rating"].mean())

