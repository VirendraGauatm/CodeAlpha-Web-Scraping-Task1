import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
data = []
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    response.encoding = "utf-8"
    print("Scraping page:", page)
    print("Status code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    print("Total books on this page:", len(books))

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.find("p", class_="star-rating")["class"][1]
        availability = book.find("p", class_="instock availability").text.strip()

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

df = pd.DataFrame(data)
df["Price"] = df["Price"].str.replace("Â£", "", regex=False).str.replace("£", "", regex=False).astype(float)
print(df.head())
print("Total books collected:", len(df))
print("Missing values:")
print(df.isnull().sum())

df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")
print("CSV file created successfully!")
