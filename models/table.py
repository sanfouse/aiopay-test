from . import db


class Advert(db.Model):

  __tablename__ = 'adverts'

  id = db.Column(db.Integer(), primary_key=True)
  category_code = db.Column(db.String(20))
  category_name = db.Column(db.String(50))

  title = db.Column(db.Unicode())
  description = db.Column(db.Unicode())
  photo = db.Column(db.Unicode())
  price = db.Column(db.Numeric(12,2))

  partner_link = db.Column(db.Unicode())


class User(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer(), primary_key=True)
  nickname = db.Column(db.Unicode(), default='noname')
  otp = db.Column(db.Integer())


async def create(app_):
    await db.gino.create_all()


