import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"

def books_to_scrape(url):
  try:

    response = requests.get(url)

    status_code = response.status_code
    booklist = []

    if status_code == 200:
      soup = BeautifulSoup(response.text,'html.parser')
      s = soup.find_all(class_='product_pod')
      for i in range(len(s)):
        book = s[i].find_all('h3')
        book = book[0].find('a')
        bookname = book["title"]
        price = s[i].find(class_="price_color").text
        price = price[1:]
        booklist.append(
        {
          'name':bookname,

          'price':price

        }


        )


      csv_file = open('books_to_scrape.csv', 'w', encoding='utf-8', newline='')

      writer = csv.writer(csv_file)

      writer.writerow(['name','price'])

      for book in booklist:
        writer.writerow(book.values())
      csv_file.close()

  except:
    print("Bad Response check the URL again")
  else:
    print("CSV file created successfully!")



books_to_scrape(url)