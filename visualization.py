import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_data.csv")

print("Dataset loaded successfully!")
print(df.head())

# Book Rating Distribution
rating_order = ["One", "Two", "Three", "Four", "Five"]
rating_counts = df["Rating"].value_counts().reindex(rating_order, fill_value=0)

plt.figure(figsize=(8, 5))
bars = plt.bar(rating_counts.index, rating_counts.values)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("chart1_rating_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# Book Price Distribution
plt.figure(figsize=(8, 5))
counts, bins, patches = plt.hist(df["Price"], bins=10, edgecolor="black")

for count, patch in zip(counts, patches):
    if count > 0:
        plt.text(
            patch.get_x() + patch.get_width() / 2,
            count,
            int(count),
            ha="center",
            va="bottom"
        )

plt.title("Distribution of Book Prices")
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("chart2_price_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# Average Price by Rating
average_price = df.groupby("Rating")["Price"].mean()
average_price = average_price.reindex(rating_order)

plt.figure(figsize=(8, 5))
bars = plt.bar(average_price.index, average_price.values)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"£{bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.title("Average Book Price by Rating")
plt.xlabel("Book Rating")
plt.ylabel("Average Price (£)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("chart3_average_price_by_rating.png", dpi=300, bbox_inches="tight")
plt.show()

# Book Rating vs Price
price_data = [df[df["Rating"] == rating]["Price"] for rating in rating_order]

plt.figure(figsize=(8, 5))
plt.boxplot(price_data, tick_labels=rating_order)
for i, prices in enumerate(price_data):
    if not prices.empty:
        median_price = prices.median()
        plt.text(i + 1, median_price, f"£{median_price:.2f}", ha="center", va="bottom")

plt.title("Book Price Distribution by Rating")
plt.xlabel("Book Rating")
plt.ylabel("Book Price (£)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("chart4_boxplot_rating_vs_price.png", dpi=300, bbox_inches="tight")
plt.show()

# Top 10 Most Expensive Books
top_books = df.nlargest(min(10, len(df)), "Price").sort_values("Price")
plt.figure(figsize=(14, 8))
bars = plt.barh(top_books["Title"], top_books["Price"])

for bar in bars:
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f" £{bar.get_width():.2f}",
        va="center"
    )

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig("chart5_top_10_expensive_books.png", dpi=300, bbox_inches="tight")
plt.show()
