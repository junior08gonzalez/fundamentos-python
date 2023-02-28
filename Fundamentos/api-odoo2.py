import xmlrpc.client
url='http://190.128.129.18:8169'
common2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
db='test_sth'
username='ecommerce.user'
password = 'testuser'
uid = common2.authenticate(db, username, password, {})
print(uid)
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
data = models.execute_kw(db, uid, password,'res.partner', 'search_read',[[['ruc', '=','4']]],{'fields': ['name', 'country_id']})
print(data)