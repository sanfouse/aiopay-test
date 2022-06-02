from views import *

def setup_routes(app):
    
    app.router.add_get('/', home)
    app.router.add_get('/admin/login', login)
    app.router.add_get('/admin/', home_admin)
    app.router.add_get('/admin/add_item', add_item)

    app.router.add_post('/admin/add_item', add_item_check)
    app.router.add_get('/admin/{data}', advert)
    app.router.add_post('/admin/{data}', edit_item)
    app.router.add_post('/admin/', log_in)
    app.router.add_post('/admin/login', log_out)
    app.router.add_get('/admin/delete/{data}', delete_item)