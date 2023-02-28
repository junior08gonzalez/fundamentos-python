import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='postgres',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'SELECT * name FROM persona WHERE id_persona IN %s'
entrada = input("Proporciona las pk a buscar (separado por comas): ")
tupla = tuple(entrada.split(','))
print(tupla)
#id_persona = 1
#id_persona = input("Proporciona la pk a buscar: ")
llaves_primarias = (tupla,)
cursor.execute(sentencia, llaves_primarias)
#PARA RECUPERAR EL RESULTADO DE LA CONSULTA O REGISTROS
registros = cursor.fetchall()
for registro in registros:
    print(registro)
#PARA RECUPERAR UN SOLO REGISTRO
#registros = cursor.fetchone()

cursor.close()
conexion.close()