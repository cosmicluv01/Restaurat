#Prising
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------- LOAD ----------
df = pd.read_csv("zomato_clean.csv")
rated = df[df["Aggregate rating"] > 0]

# ---------- PRICING ----------
print("\n--- PRICING ---")
print(df["Currency"].value_counts().head())

inr = rated[rated["Currency"] == "Indian Rupees(Rs.)"].copy()
print("Indian restaurants:", len(inr))
print(inr["Average Cost for two"].describe())
print(inr[["Average Cost for two", "Aggregate rating", "Votes"]].corr())

inr["Price Range"] = pd.cut(inr["Average Cost for two"],
                            bins=[0, 300, 600, 1000, 5000, 100000],
                            labels=["Budget", "Low", "Mid", "High", "Luxury"])
print(inr.groupby("Price Range", observed=True)["Aggregate rating"].agg(["mean", "count"]))

# ---------- CUISINES ----------
print("\n--- CUISINES ---")
cuisines = df.assign(Cuisine=df["Cuisines"].str.split(",")).explode("Cuisine")
cuisines["Cuisine"] = cuisines["Cuisine"].str.strip()
cuisines = cuisines[cuisines["Cuisine"] != "Unknown"]

print(cuisines["Cuisine"].value_counts().head(10))

cr = cuisines[cuisines["Aggregate rating"] > 0].groupby("Cuisine")["Aggregate rating"].agg(["mean", "count"])
print(cr[cr["count"] >= 50].sort_values("mean", ascending=False).head(10))