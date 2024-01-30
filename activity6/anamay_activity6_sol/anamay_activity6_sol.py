'''
Written By - Anamay Dubey
Date = 30/01/24
Title = Activity 6 Solution 
'''

from bs4 import BeautifulSoup
import requests
import csv

URL = 'http://books.toscrape.com/'
webpage = requests.get(URL)  #request http response

if webpage.status_code == 200: #200 is for succesfull response
    soup = BeautifulSoup(webpage.content, 'html.parser')
    Books = soup.find_all(class_='product_pod') #find all mentioned tags

    data = [] # empty list to append all scrapped data

    for book in Books: #iterating over all soup objects and retrieving title and price tag
        title = book.find('h3').find('a')['title']
        price = book.find(class_='price_color').get_text().replace("£", "")
        data.append({'Title': title, 'Price': price}) # append the scrapped data in empty list

    with open("report.csv", "w", encoding="UTF-8", newline="") as file: #create csv file
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Title', 'Price'])

        for book in data: #appending data elments in csv file
            csv_writer.writerow(book.values()) #only append values

else:
    print("Something went wrong. Check your URL or internet connection.")
