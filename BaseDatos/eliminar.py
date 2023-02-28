import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='postgres',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona = %s'
#valores = (9,)
entrada = input("Proprociona la pk a eliminar: ")
cursor.execute(sentencia, entrada)
#guarda informacion en la base de datos
conexion.commit()
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

cursor.close()
conexion.close()