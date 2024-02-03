import requests
import csv
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all(class_='product_pod')
    data = []
    
    for book in books:
        name = book.h3.a['title']
        price = book.find(class_='price_color').text
        data.append({'name': name, 'price': price})
    
    with open('soniya.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price'])
        writer.writeheader()
        
        for row in data:
            writer.writerow(row)
