#!/usr/bin/python3
"""
Usage: editar.py lista
       editar.py anadir NOMBRE [ANIO MES DIA_DEL_MES HORA MINUTO]
       editar.py eliminar POS
       editar.py modificar POS NOMBRE [ANIO MES DIA_DEL_MES HORA MINUTO]

Options:
-h --help   Mostrar esta pantalla.
--creditos  Mostrar los creditos.
--version   Mostrar version.
"""

from docopt import docopt
from time import localtime
from datos import GestorLista, Recordatorio
from base_datos import cargar, guardar
t = localtime()

recordatorios = GestorLista()

if __name__ == '__main__':
    """Poner todos los argumentos en una lista.
    Se utiliza la libreria docopt."""
    cargar(recordatorios)

    argumentos = docopt(__doc__, version='0.0.0')

    # pasar los argumentos a su variable
    # y si no se han dado ponerlos por defecto
    nombre = argumentos['NOMBRE']

    if argumentos['ANIO'] is None:
        anio = t.tm_year
    else:
        anio = argumentos['ANIO']

    if argumentos['MES'] is None:
        mes = t.tm_mon
    else:
        mes = argumentos['MES']

    if argumentos['DIA_DEL_MES'] is None:
        mdia = t.tm_mday
    else:
        mdia = argumentos['DIA_DEL_MES']

    if argumentos['HORA'] is None:
        hora = t.tm_hour
    else:
        hora = argumentos['HORA']

    if argumentos['MINUTO'] is None:
        minu = 0
    else:
        minu = argumentos['MINUTO']

    # todos las opciones de los argumentos
    if argumentos['lista']:
        for i in range(0, len(recordatorios.lista)):
            print("[" + str(i) + "]" + " ", end='')
            for j in recordatorios.lista[i].mostrar():
                print(str(j) + " ", end='')
            print("")

    if argumentos['anadir']:
        recordatorios.anadir(nombre, anio, mes, mdia, hora, minu)

    if argumentos['eliminar']:
        recordatorios.eliminar(int(argumentos['POS']))

    if argumentos['modificar']:
        recordatorios.lista[int(argumentos['POS'])].modificar(nombre, anio,
                                                              mes, mdia,
                                                              hora, minu)
    guardar(recordatorios)
