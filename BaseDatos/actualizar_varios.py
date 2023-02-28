import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='postgres',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
valores = (
    ('Juan', 'Perez', 'jperez@gmail.com',1),
    ('Karla1', 'Gomez2', 'kgomez3@gmail.com',2)   
)
#executemany cuando vamos a hacer una transaccion con varios registros 
cursor.executemany(sentencia, valores)
#guarda informacion en la base de datos
conexion.commit()
registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

cursor.close()
conexion.close()