import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Sat_Sharma_politician&tbm=isch&hl=en&tbs=isz:l&sa=X&ved=2ahUKEwjP2IzQkK7xAhVO0RoKHT6UDSMQBXoECAEQGQ&biw=1080&bih=809'

# page = open('tower.html', 'r').read()
page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')

print(soup)
# for raw_img in soup.find_all('img'):
#     link = raw_img.get('src')
#     if link:
#         print(link)
