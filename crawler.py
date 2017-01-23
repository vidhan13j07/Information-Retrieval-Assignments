from bs4 import BeautifulSoup
import os
import requests

link = input('Enter the link: ')
path = os.getcwd()
filename = input('Enter the filename: ')

r = requests.get(link)

soup = BeautifulSoup(r.text, 'html.parser')
with open(path + '/' + filename, 'w') as f:
    f.write(soup.get_text())
