import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='postgres',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona ORDER BY id_persona DESC'
cursor.execute(sentencia)
#PARA RECUPERAR EL RESULTADO DE LA CONSULTA O REGISTROS
registros = cursor.fetchall()
print(registros)
cursor.close()
conexion.close()