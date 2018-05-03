from bs4 import BeautifulSoup
soup = BeautifulSoup(open('scenery.html'), 'lxml')
print(soup.prettify)

tag1 = soup.ul
print(tag1)
print(soup.find('ul'))

print(soup.find_all('ul'))
print(soup.find_all('ul')[0])
print(soup.find('li',attrs={'nu':'3'}))
print(soup.find_all('a',attrs={'class':'price'}))
