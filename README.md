# Amazon.in Product Price Scraper

This project is a Python script that scrapes **product details like title, price, rating, and availability** from [Amazon.in](https://www.amazon.in) based on a given search query. The results are saved into a `.csv` file.

---

## Features

-  Search any product on Amazon.in
-  Extract product title, price, rating, and availability
-  Save scraped data to a CSV file
-  Lightweight and easy to customize

---

## Sample Output (CSV)

| Title                         | Price | Rating | Availability     |
|------------------------------|-------|--------|------------------|
| Apple iPhone 14 (128 GB)     | 65999 | 4.5    | Available        |
| Apple iPhone 14 Pro Max      | 139900| 4.6    | Available        |

---

##Requirements

Install the required Python libraries using pip:

```bash
pip install requests beautifulsoup4