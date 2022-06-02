from bs4 import BeautifulSoup
import requests

class GetAliItem:
    """Parse AliExpress"""
    def __init__(self, url) -> None:
        self.url = url
        self.header = {'user-agent': 'hii'}
        self.soup = BeautifulSoup(requests.get(
            url=url,
            headers=self.header).text, 'lxml')

    def get_image(self):
        try:
            result = self.soup.find('div', class_='Product_Gallery__imgWrapper__9bm18').find('img')
            return result['src']
        except:
            return 'https://avatarko.ru/img/kartinka/1/avatarko_anonim.jpg'

