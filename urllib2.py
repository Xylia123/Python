from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)
print soup.html.head.title.string