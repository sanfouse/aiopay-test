import pathlib

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from models import PG_URL, db
from models.table import create
from routes import setup_routes

BASE_DIR = pathlib.Path(__file__).parent.parent

app = web.Application(middlewares=[db])
db.init_app(app, dict(dsn=PG_URL))

app.on_startup.append(create)

if __name__ == '__main__':
    aiohttp_jinja2.setup(app,
        loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiopay-test' / 'templates')))
    setup(app,
        EncryptedCookieStorage(b'Thirty  two  length  bytes  key.'))    
    setup_routes(app)
    web.run_app(app, host='127.0.0.1')

