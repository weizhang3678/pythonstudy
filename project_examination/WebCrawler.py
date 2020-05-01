import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_links(url):
    soup = get_page(url)
    links_div = soup.find_all('div', class_="content__list--item--main")
    links = [div.a.get('href') for div in links_div]
    return links

house_url = "https://bj.lianjia.com/zufang/zufang/BJ2500105086433771520.html";
soup = get_page(house_url)
text = soup.find('div', class_='content__aside--title').text
