import requests
from bs4 import BeautifulSoup
import csv

#Search query
query = "iphone 14"

url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to fetch page. Status code:", response.status_code)
    exit()

soup = BeautifulSoup(response.content, "html.parser")

products = soup.find_all("div", {"data-component-type": "s-search-result"})

all_data = []

for product in products:
    try:
        title = product.h2.text.strip()

        price_tag = product.select_one("span.a-price-whole")
        price = price_tag.text.strip().replace(",", "") if price_tag else "N/A"

        rating_tag = product.select_one("span.a-icon-alt")
        rating = rating_tag.text.strip().split(" ")[0] if rating_tag else "N/A"

        availability = "Available" if price != "N/A" else "Out of Stock"

        all_data.append([title, price, rating, availability])

    except Exception as e:
        print("Error:", e)
        continue

with open("amazon_products.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price (INR)", "Rating", "Availability"])
    writer.writerows(all_data)

print(f"Scraped {len(all_data)} products and saved to 'amazon_products.csv'")