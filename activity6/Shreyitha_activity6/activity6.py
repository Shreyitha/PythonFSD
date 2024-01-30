import requests
import bs4
import csv

res=requests.get('http://books.toscrape.com/')
soup=bs4.BeautifulSoup(res.text,'html.parser')

if res.status_code == 200:
    links=soup.find_all(class_='product_pod')
    Book_record=[]
    for link in links:
        title = link.find('h3').find('a')['title']
        price = link.find(class_='price_color').get_text()
        Book_record.append({'Title': title, 'Price': price.replace('Â','')})
    # print(Book_record)


    file= open('booksdetails.csv', 'w', encoding='utf-8', newline='')
    writer=csv.writer(file)

    writer.writerow(['name','price'])

    for book in Book_record:
        writer.writerow(book.values())
    file.close()

else:
    print('Failed to scrap data from the website')





