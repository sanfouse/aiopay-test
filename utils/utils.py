import requests
from bs4 import BeautifulSoup


class AliItem:
    """Parse AliExpress Item"""
    def __init__(self, url) -> None:
        self.header = {'user-agent': 'asdsdadsa'}
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
            result: str = self.soup.find('div', class_="ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 price ali-kit_Price__size-xl__12ybyf Product_Price__current__1uqb8 product-price-current").text
            return int(result.split(',')[0].replace(u'\xa0', u''))
        except:
            return 123

    def get_(self):
        try:
            pass
        except:
            pass

def check_url_status(request):
    try:
        search = request.rel_url.query['search']
    except:
        search = None

    try:
        category = request.rel_url.query['category']
    except:
        category = None
    
    return [search, category]