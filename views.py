import aiohttp_jinja2
from aiohttp import web
from aiohttp_session import get_session
from utils.utils import get_image
from models.table import Advert, User


@aiohttp_jinja2.template('home.html')
async def home(request):
    session = await get_session(request)
    try:
        if session['auth']:
            if str(request.url.relative()).startswith('/admin/?search='):
                search: str =  request.rel_url.query['search']
                data = await Advert.query.where(Advert.title.startswith(str(search))).gino.all()
                return {'data': data[::-1]}
            data = await Advert.query.gino.all()
            return {'data': data[::-1], 'id': str(session['id'])}
        else:
            raise web.HTTPFound('/admin/login')
    except KeyError:
        raise web.HTTPFound('/admin/login')


@aiohttp_jinja2.template('login.html')
async def login(request):
    session = await get_session(request)
    session['auth'] = False


@aiohttp_jinja2.template('login.html')
async def log_out(request):
    session = await get_session(request)
    try:
        if session['auth']:
            session['auth'] = False
            session['id'] = None
            raise web.HTTPFound('/admin/login')
        else:
            raise web.HTTPFound('/admin/login')
    except KeyError:
        raise web.HTTPFound('/admin/login')


@aiohttp_jinja2.template('home.html')
async def log_in(request):
    session = await get_session(request)
    data = await request.post()
    try:
        user_data = await User.query.where(User.otp==int(data['otp'])).gino.scalar()
    except ValueError:
        raise web.HTTPFound('/admin/login')

    if user_data is None:
        session['auth'] = False
        raise web.HTTPFound('/admin/login')

    if int(data['id']) not in [895872844]:
        session['auth'] = False
        raise web.HTTPFound('/admin/login')
    
    session['auth'] = True
    session['id'] = data['id']
    raise web.HTTPFound('/admin/')


@aiohttp_jinja2.template("item.html")
async def advert(request):
    session = await get_session(request)
    try:
        if session['auth']:
            data = str(request.url.relative()).split('/')[2]
            founding_advert = await Advert.query.where(Advert.id == int(data)).gino.first()
            return {'item': founding_advert, 'message': 'Редактирование товара', 'id': str(session['id'])}    
        else:
            raise web.HTTPFound('/admin/login')
    except KeyError:
        raise web.HTTPFound('/admin/login')


@aiohttp_jinja2.template("item.html")
async def edit_item(request):
    session = await get_session(request)
    try:
        if session['auth']:
            data = await request.post()
            item = await Advert.query.where(Advert.id == int(data['id'])).gino.first()
            await item.update(title=data['title'],
                description=data['description'],
                price=data['price'], partner_link=data['link'],
                category_name=data['category'],
                category_code=str(data['category']).lower().replace(' ', '_'),
                image_link=str(get_image(str(data['link'])))).apply()
            raise web.HTTPFound('/admin/')
        else:
            raise web.HTTPFound('/admin/login')
    except KeyError:
        raise web.HTTPFound('/admin/login')


@aiohttp_jinja2.template('item.html')
async def add_item(request):
    session = await get_session(request)
    try:
        if session['auth']:
            return {'item': None, 'message': 'Добавление товара', 'id': str(session['id'])}
        else:
            raise web.HTTPFound('/admin/login')
    except KeyError:
        raise web.HTTPFound('/admin/login')


@aiohttp_jinja2.template('item.html')
async def add_item_check(request):
    session = await get_session(request)
    try:
        if session['auth']:
            data = await request.post()
            await Advert.create(title=data['title'],
                description=data['description'],
                price=data['price'], 
                partner_link=data['link'],
                category_name=data['category'],
                category_code=str(data['category']).lower().replace(' ', '_'),
                image_link=str(get_image(str(data['link']))))

            raise web.HTTPFound('/admin/')
        else:
            raise web.HTTPFound('/admin/login')
    except KeyError:
        raise web.HTTPFound('/admin/login')


@aiohttp_jinja2.template('home.html')
async def delete_item(request):
    session = await get_session(request)
    try:
        if session['auth']:
            data = str(request.url.relative()).split('/')[3]
            await Advert.delete.where(Advert.id == int(data)).gino.first()
            raise web.HTTPFound('/admin/')
        else:
            raise web.HTTPFound('/admin/login')
    except KeyError:
        raise web.HTTPFound('/admin/login')