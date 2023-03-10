from conexion import Conexion
from logger_base import logger

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    #inicio de with
    def __enter__(self):
        logger.debug('Inicio de with metodo __enter__')
        self.__conn = Conexion.obtenerConexion() 
        self.__cursor = self.__conn.cursor()
        logger.debug(f'Inicio de with metodo __enter__ {self.__conn}')
        return self.__cursor
        
    #fin del bloque with
    def __exit__(self,exception_type, exception_value,exception_traceback):
        logger.debug('Se ejecuta metodo __exit__()')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrio una excepcion: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug(f'Commit de la transaccion')
        #Cerramos el cursor
        self.__cursor.close()
        #Regresar la conexion al pool
        Conexion.liberarConexion(self.__conn)
        
        
if __name__ == '__main__':
    #Obtenemos un cursor a partir de la conexion del pool
    #with se ejecuta __enter__ y termina con __exit__
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM persona')
        logger.debug('Listado de personas')
        logger.debug(cursor.fetchall())