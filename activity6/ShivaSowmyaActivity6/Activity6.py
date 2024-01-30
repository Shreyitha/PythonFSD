import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('http://books.toscrape.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.select('.product_pod')
    data = []
    for book in books:
        title = book.h3.a['title']
        price = book.select('p.price_color')[0].get_text(strip=True)
        price=price[1:]
        data.append({'name': title, 'price': price})

    with open('books.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csvwriter = csv.DictWriter(csv_file, fieldnames=['name', 'price'])
        csvwriter.writeheader()
        csvwriter.writerows(data)
else:
    print("Failed to retrieve data. Status code: %s" %response.status_code)
