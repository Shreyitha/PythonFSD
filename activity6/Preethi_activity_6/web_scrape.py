import requests
from bs4 import BeautifulSoup
import  csv
url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    books= soup.find_all( class_='product_pod')
    book_data = []
    for book in books:
        title_element = book.select_one('h3 a')
        title = title_element.get('title')
        price = book.select_one('.price_color').text.strip()
        book_data.append({'Title': title, "Price":price})

    with open('books.csv', 'w', newline="") as csvfile:
        csv_write = csv.writer(csvfile)


        csv_write.writerow(['Title', 'Price']) 
        for book in book_data:
            csv_write.writerow([book['Title'], book['Price']])

    print("Scaping and writing completed")


