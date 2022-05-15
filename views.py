import random

import aiohttp_jinja2
from aiohttp import web
from models.table import Advert, User
# from utils import loader


@aiohttp_jinja2.template('home.html')
async def home(request):
    data = await Advert.query.gino.all()
    return {'data': data}


@aiohttp_jinja2.template('home.html')
async def search_item(request):
    search: str = request.rel_url.query['search']
    data = await Advert.query.where(Advert.title.startswith(search)).gino.all()
    return {'data': data}


@aiohttp_jinja2.template("item.html")
async def advert(request):
    data = await request.post()
    founding_advert = await Advert.query.where(Advert.id == int(*data)).gino.first()
    return {'item': founding_advert}


@aiohttp_jinja2.template("home.html")
async def advert_change(request):
    data = await request.post()
    item = await Advert.query.where(Advert.id == int(data['id'])).gino.first()

    await item.update(title=data['title'],
        description=data['description'],
        price=data['price'], partner_link=data['link'],
        category_name=data['category'],
        category_code=str(data['category']).lower().replace(' ', '_')).apply()

    raise web.HTTPFound('/admin')


# @aiohttp_jinja2.template("signup_id.html")
# async def auth_id(request):
#     pass


# @aiohttp_jinja2.template("signup_otp.html")
# async def auth_confirm_password(request):
#     data = await request.post()
#     number = list('1234567890')
#     otp = ''
#     item = await User.query.where(User.id == int(data['id'])).gino.first()
#     for i in range(4):
#         otp += random.choice(number)
#     await item.update(otp=int(otp)).apply()
#     await loader.bot.send_message(text=otp, chat_id=int(data['id']))
