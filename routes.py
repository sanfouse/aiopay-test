from views import *

def setup_routes(app):
    app.router.add_get('/admin', home)
    app.router.add_get('/admin/', search_item)
    app.router.add_post('/admin', advert_change)
    app.router.add_post('/admin/edit_item', advert)
    # app.router.add_get('/auth', auth_id)
    # app.router.add_post('/auth/confirm', auth_confirm_password)
