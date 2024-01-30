import requests
from bs4 import BeautifulSoup
import csv

# 1. Import the requests and BeautifulSoup libraries

# 2. Define the URL of the Books to Scrape website as a variable
url = "http://books.toscrape.com/"

# 3. Send a GET request to the URL and store the response object
response = requests.get(url)

# 4. Check if the status code of the response is 200 (OK)
if response.status_code == 200:
    # 5. Parse the HTML content of the response using BeautifulSoup and specify the parser as ‘html.parser’
    soup = BeautifulSoup(response.text, 'html.parser')

    # 6. Find all the book elements using the class name ‘product_pod’
    books = soup.find_all(class_='product_pod')

    # 8. Store the extracted data in a list of dictionaries
    book_data = []
    for book in books:
        title = book.h3.a['title']
        price = book.select('p.price_color')[0].text
        book_data.append({'Title': title, 'Price': price})

    # 9. Import the csv library and open a new CSV file in write mode
    with open('best_selling_books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # 10. Create a csv writer object and write the header row with the column names
        fieldnames = ['Title', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 11. Write the data rows using the writerow method
        for data in book_data:
            writer.writerow(data)

    print("Data has been successfully scraped and saved to 'best_selling_books.csv'")

else:
    print("Failed to retrieve the page. Status code:", response.status_code)