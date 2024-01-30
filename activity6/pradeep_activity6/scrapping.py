import requests
from bs4 import BeautifulSoup
import csv

web_url = "http://books.toscrape.com/"

response = requests.get(web_url)

if response.status_code == 200:
    print("Status code is 200 (OK)")
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all(class_="product_pod")
    
    bookscrap = []
    for book in books:
         title = book.find('h3').find('a')['title']
         price = book.find(class_='price_color').get_text().replace("£", "")
         bookscrap.append({'title':title,'price':price})

    with open("book_scrap.csv","w",encoding="UTF-8",newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['title','price'])

        for book in bookscrap:
            csv_writer.writerow(book.values()) 
else:
    print(f"Status code is {response.status_code}")

