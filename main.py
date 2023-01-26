import requests
from bs4 import BeautifulSoup
import csv

# specify the URL to scrape
url = 'https://www.amazon.com/s?k=laptops'

# make a request to the website
response = requests.get(url)

# parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# create an empty list to store the data
data = []

# find all the elements with the class 's-result-item'
for element in soup.find_all(class_='s-result-item'):
    # extract the title of the product 
    title = element.find(class_='a-size-medium a-color-base a-text-normal').get_text()
    # extract the price of the product
    price = element.find(class_='a-price-whole').get_text()
    # extract the availability of the product
    availability = element.find(class_='a-size-base a-color-secondary').get_text()
    # append the title, price, availability to the data list
    data.append([title, price, availability])

# write the data to a CSV file
with open('amazon_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Price", "Availability"])
    writer.writerows(data)

print("Data saved to amazon_data.csv")
