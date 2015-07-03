"""Este modulo sirve para modificar lista general de recordatorios."""

from datos import GestorLista, Recordatorio
from base_datos import cargar, guardar

recordatorios = GestorLista()


def lista():
    cargar(recordatorios)
    rec_list = []
    del rec_list[:]
    for i in range(0, len(recordatorios.lista)):
        rec_list.append([])
        for j in recordatorios.lista[i].mostrar():
            rec_list[i].append(j)
    return rec_list


def anadir(nombre, anio, mes, mdia, hora, minu):
    cargar(recordatorios)
    recordatorios.anadir(nombre, anio, mes, mdia, hora, minu)
    guardar(recordatorios)


def eliminar(pos):
    cargar(recordatorios)
    recordatorios.eliminar(pos)
    guardar(recordatorios)


def modificar(pos, nombre, anio, mes, mdia, hora, minu, recordado=None):
    cargar(recordatorios)
    recordatorios.lista[pos].modificar(nombre, anio, mes, mdia, hora, minu, recordado)
    guardar(recordatorios)
