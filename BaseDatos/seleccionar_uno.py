import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='postgres',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
#id_persona = 1
id_persona = input("Proporciona la pk a buscar: ")
llave_primaria = (id_persona,)
cursor.execute(sentencia, llave_primaria)
#PARA RECUPERAR EL RESULTADO DE LA CONSULTA O REGISTROS
#registros = cursor.fetchall()
#PARA RECUPERAR UN SOLO REGISTRO
registros = cursor.fetchone()
print(registros)
cursor.close()
conexion.close()