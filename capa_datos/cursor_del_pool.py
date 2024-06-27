from capa_datos.conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f"inicio del motodo with __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback_excepcion):
        log.debug(f"se ejecuta metodo __exit__")
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"ocurrio una excepcion: {valor_excepcion} {tipo_excepcion}, {traceback_excepcion}")
        else:
            self._conexion.commit()
            log.debug(f"commit de la transaction")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug(f"dentro delo bloque with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())