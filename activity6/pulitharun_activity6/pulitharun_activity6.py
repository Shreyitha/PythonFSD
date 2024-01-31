from bs4 import BeautifulSoup
import requests
import csv

URL = 'http://books.toscrape.com/'
r = requests.get(URL)  

if r.status_code == 200: 
    soup = BeautifulSoup(r.content, 'html.parser')
    Books = soup.find_all(class_='product_pod') 
    books = [] 
    for book in Books: 
        title = book.find('h3').find('a')['title']
        price = book.find(class_='price_color').get_text().replace("£", "")
        books.append({'Title': title, 'Price': price}) #
    with open("bestselling.csv", "w", encoding="UTF-8", newline="") as csv_file: 
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Title', 'Price'])
        for book in books: 
            csv_writer.writerow(book.values()) 

    print("Books data saved")

else:
    print('Failed to scrap data from the website')