from persona import Persona
from cursor_del_pool import CursorDelPool
from logger_base import logger

class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Update-Delete entidad Persona
    '''
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre =%s, apellido =%s, email=%s WHERE id_persona = %s'
    __ELIMINAR =  'DELETE FROM persona WHERE id_persona =%s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1], registro[2],registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.getNombre(), persona.getApellido(),persona.getEmail())
            cursor.execute(cls.__INSERTAR,valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.getNombre(), persona.getApellido(),persona.getEmail(),persona.getId())
            cursor.execute(cls.__ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.getId(),)
            cursor.execute(cls.__ELIMINAR,valores)
            return cursor.rowcount
    
if __name__ == '__main__':
    #Listado de personas
    # personas = PersonaDao.seleccionar()
    # for persona in personas:
    #     logger.debug(persona)
    #Insertar un nuevo Registro:
    # persona = Persona(nombre = 'Pedro', apellido = 'Najera', email = 'pnajera@gmail.com')
    # personas_insertadas = PersonaDao.insertar(persona)
    # logger.debug(f'Personas insertados: {personas_insertadas}')
    
    #Actualizar un registro existente
    # persona = Persona(1,'Juan1', 'Perez2','jperez3@gmail.com')
    # persona_actualizada = PersonaDao.actualizar(persona)
    # logger.debug(f'Personas actualizadas: {persona_actualizada}')
    
    #eliminar un registro persona
    persona2 = Persona(5)
    personas_eliminadas = PersonaDao.eliminar(persona2)
    logger.debug(f'Personas eliminadas: {personas_eliminadas}')