import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all(class_='product_pod')

    book_data = []

    for book in books:
        title = book.h3.a['title']
        price = book.select_one('div p.price_color').get_text(strip=True)
        price=price[1:]
        book_data.append({'name': title, 'price': price})

    with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in book_data:
            writer.writerow(row)

    print("Data successfully scraped and saved to 'books.csv'")
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
