import requests
from bs4 import BeautifulSoup


class AliItem:
    """Parse AliExpress Item"""
    def __init__(self, url) -> None:
        self.header = {'user-agent': 'hii'}
        self.soup = BeautifulSoup(requests.get(
            url=url,
            headers=self.header).text, 'lxml')

    def get_image(self):
        try:
            return self.soup.find('div', class_='Product_Gallery__imgWrapper__9bm18').find('img')['src']
        except:
            return 'https://avatarko.ru/img/kartinka/1/avatarko_anonim.jpg'

    def get_price(self):
        try:
            result: str = self.soup.find('div', class_="Product_Price__container__1uqb8 product-price").text
            return int(result.split(',')[0].replace(u'\xa0', u''))
        except:
            return 123

    def get_delivery_status(self):
        try:
            pass
        except:
            pass

