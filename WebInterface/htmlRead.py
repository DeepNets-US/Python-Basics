from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
html_page = urlopen(url)
html_text = html_page.read().decode()
print(html_text)
