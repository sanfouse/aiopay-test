from gino.ext.aiohttp import Gino

db = Gino()

PG_URL = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
    host="localhost",
    port=5432,
    user='postgres',
    password=15610348,
    database="postgres",
)

