import requests
from bs4 import BeautifulSoup


#  1 - Collect and parse first page
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# 4 - Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()


# 2 - Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

# 2 - Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

# 3 - create a loop to print out all artists' names
#for artist_name in artist_name_list_items:
#   print(artist_name.prettify())

# 5 - use .content to pull out the <a> tag's children
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    print(names)
    print(links)

