from bs4 import BeautifulSoup
import requests

# Set URL
url = "https://www.binance.com/en/trade/TRX_USDT"

# Establish connection to URL
response = requests.get(url)

# Assign response html to variable data
data = response.text

# parse data to HTML with beatiful soup and assign to soup
soup = BeautifulSoup(data,'html.parser')

# search soup for CSS / tags
tags = soup.find_all('a')

titles = soup.find_all("a",{"class":"result-title"})
adresses = soup.find_all("span",{"class":"result-hood"})

for title in titles:
    print(title.text)

for adress in adresses:
    print(adress.text)
