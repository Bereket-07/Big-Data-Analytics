import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def basic_data_cleaning(df):
    print("handle missing values:")
    df.ffill(inplace=True)
    print("missing values handeled successfully")
    print("remove duplicates:")
    df.drop_duplicates(inplace=True)
    print("duplicates removed successfully")
def distribution_of_price(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(df["price"], bins=50, kde=True, color="blue")
    plt.title("Distribution of Product Prices")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.show()
def price_vs_rating(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="price", y="reviews", alpha=0.5)
    plt.title("Price vs. Rating")
    plt.xlabel("Price")
    plt.ylabel("Rating")
    plt.show()
def expensive_catagory_name(df):
    plt.figure(figsize=(12, 6))
    top_categories = df.groupby("categoryName")["price"].sum().nlargest(10)
    top_categories.plot(kind="bar", color="green")
    plt.title("Top 10 Product Categories by price")
    plt.xlabel("Category")
    plt.ylabel("Total price")
    plt.xticks(rotation=45)
    plt.show()


