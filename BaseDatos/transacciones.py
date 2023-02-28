import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='postgres',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')
try:
    #conexion.autocommit = True
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan1', 'Perez2', 'jperez3@gmail.com',1)
    cursor.execute(sentencia, valores)
    
    #guarda informacion en la base de datos
    conexion.commit()
except psycopg2.OperationalError as e:
    #rollback da marcha atras a todas las operaciones pendientes
    conexion.rollback()
    print(f"Ocurrio un error en la transaccion: {e} ")
finally:
    cursor.close()
    conexion.close()