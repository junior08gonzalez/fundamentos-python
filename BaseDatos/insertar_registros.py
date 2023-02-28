import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='postgres',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)'

valores = (
     ('Marcos', 'Cantu', 'cmarcos@gmail.com'),
     ('Angel', 'Quintana', 'aquintana@gmail.com'),
     ('Maria', 'Gonzalez', 'mgonzalez@gmail.com')
 )
#executemany cuando vamos a hacer una transaccion con varios registros 
cursor.executemany(sentencia, valores)
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()