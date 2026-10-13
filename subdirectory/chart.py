import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("zomato_clean.csv")
rated = df[df["Aggregate rating"] > 0]

# 1. Rating distribution
plt.figure(figsize=(8, 5))
sns.histplot(rated["Aggregate rating"], bins=20, kde=True)
plt.title("Rating Distribution")
plt.savefig("rating_distribution.png", dpi=150, bbox_inches="tight")
plt.show()

# 2. Price range vs rating (INR)
inr = rated[rated["Currency"] == "Indian Rupees(Rs.)"].copy()
inr["Price Range"] = pd.cut(inr["Average Cost for two"],
                            bins=[0, 300, 600, 1000, 5000, 100000],
                            labels=["Budget", "Low", "Mid", "High", "Luxury"])
plt.figure(figsize=(8, 5))
inr.groupby("Price Range", observed=True)["Aggregate rating"].mean().plot(kind="bar")
plt.title("Average Rating by Price Range (INR)")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)
plt.savefig("price_vs_rating.png", dpi=150, bbox_inches="tight")
plt.show()

# 3. Top 10 cuisines
cuisines = df.assign(Cuisine=df["Cuisines"].str.split(",")).explode("Cuisine")
cuisines["Cuisine"] = cuisines["Cuisine"].str.strip()
cuisines = cuisines[cuisines["Cuisine"] != "Unknown"]
top = cuisines["Cuisine"].value_counts().head(10)

plt.figure(figsize=(8, 5))
top.plot(kind="barh")
plt.gca().invert_yaxis()
plt.title("Top 10 Cuisines")
plt.savefig("top_cuisines.png", dpi=150, bbox_inches="tight")
plt.show()

# 4. Top 10 cuisines by rating (kam se kam 50 restaurants)
cr = cuisines[cuisines["Aggregate rating"] > 0].groupby("Cuisine")["Aggregate rating"].agg(["mean", "count"])
best = cr[cr["count"] >= 50].sort_values("mean", ascending=False).head(10)

plt.figure(figsize=(8, 5))
best["mean"].plot(kind="barh")
plt.gca().invert_yaxis()
plt.title("Top Rated Cuisines (50+ restaurants)")
plt.savefig("best_cuisines.png", dpi=150, bbox_inches="tight")
plt.show()