import requests, csv
from bs4 import BeautifulSoup

url='https://books.toscrape.com/'

response= requests.get(url)
if response.status_code== 200:
    soup= BeautifulSoup(response.content, 'html.parser')
    book_elements=soup.select('.product_pod')
    
    extract=[]
    
    for book in book_elements:
        name_element= book.select_one('h3 a')
        name= name_element.get('title')
        price= book.select_one('.price_color').text
        extract.append({'Name':name, 'Price':price})

file = open('Sangeeth_Books.csv','w')
writer= csv.DictWriter(file, fieldnames=['Name', 'Price'])
writer.writeheader()
for i in extract:
    writer.writerow(i)
file.close()   
  
