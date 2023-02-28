"""
XML-RPC es un método de llamada a procedimiento remoto que utiliza 
XML pasado a través de HTTP (S) como transporte. Con él, un cliente 
puede llamar a métodos con parámetros en un servidor remoto (el servidor
es nombrado por un URI) y recuperar datos estructurados. Este módulo
admite la escritura de código de cliente XML-RPC; maneja todos los 
detalles de la traducción entre objetos Python compatibles y XML en 
el cable.
"""
import xmlrpc.client
srv = 'http://localhost:8069'
#ServerProxy es un objeto que gestiona la comunicación con un servidor XML-RPC remoto
common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % srv)
print(common.version())

url='https://www.sati.com.py'
common2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common2.version())

#info = xmlrpc.client.ServerProxy('https://www.sati.com.py')
#print(info['database'])

db='sati'
username='arturo.gonzalez@sati.com.py'
password = 'Sati3212019'
uid = common2.authenticate(db, username, password, {})
print(f'Id del Usuario: {uid}')

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#Verificamos si tenemos acceso de lectura al modelo
read_acces_res_partner = models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})
print(f'Tengo acceso de lectura al modulo contacto: {read_acces_res_partner}')

#obtenemos lista de id de la bd 
ids_res_partner = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]])
print(f'Lista de id del modulo contacto: {ids_res_partner}')

#Obtenemos los datos en base al rol del usuario limitamos el resultado hasta 5
data = models.execute_kw(db, uid, password,
    'res.partner', 'search_read',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'fields': ['name', 'country_id'], 'limit': 5})

print(f'Datos obtenidos: {data}')
