import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)

username = 'zeus'
password = 'ThunderDuder'

# Acces the form

form = page.soup.find('form', {'action': '/login'})
inputs = form.find_all('input')

# Fill the form
for i in inputs:
    if i.get('name') == 'username':
        i['value'] = username
    elif i.get('name') == 'password':
        i['value'] = password
        
# Submit the form
profile_page = browser.submit(form, url = page.url)

# Confirm
print(f'Profile Page URL: {profile_page.url}')