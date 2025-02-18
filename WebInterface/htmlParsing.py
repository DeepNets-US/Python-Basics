from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html_text = page.read().decode('utf-8')
soup = BeautifulSoup(html_text, 'html.parser')

# Find all paragraphs
paras = soup.find_all('p')
# print(paras)

# Find all images
imgs = soup.find_all('img')
print(imgs)

# Lets extracy some info
for img in imgs:
    print(f'Name: {img.name}')
    print(f'Src : {img["src"]}')


# Using tag properties
print(f'Title Tag Property: {soup.title}')
