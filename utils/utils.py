from bs4 import BeautifulSoup
import requests

header = {'user-agent': 'hii'}

def get_image(url):
    try:
        response = requests.get(
            url=url,
            headers=header).text
        soup = BeautifulSoup(response, 'lxml')
        result = soup.find('div', class_='Product_Gallery__imgWrapper__9bm18').find('img')
        return result['src']
    except:
        return 'https://avatarko.ru/img/kartinka/1/avatarko_anonim.jpg'
