import time

t = time.localtime()


class Recordatorio:
    """Crea todas las propiedades del recordatorios."""
    def __init__(self, nombre, anio, mes, mdia, hora, minu, recordado=False):
        # propiedades del recordatorio
        self.nombre = nombre
        self.anio = anio
        self.mes = mes
        self.mdia = mdia
        self.hora = hora
        self.minu = minu
        self.recordado = recordado

    def comprobar(self, t):
        """Devuelve True si el recordatorio esta pasando y False si no."""
        if self.recordado == False:
            self.recordar = 0

            if self.anio == t.tm_year:
                self.recordar += 1
            if self.mes == t.tm_mon:
                self.recordar += 1
            if self.mdia == t.tm_mday:
                self.recordar += 1
            if self.hora == t.tm_hour:
                self.recordar += 1
            if self.minu == t.tm_min:
                self.recordar += 1

            if self.recordar == 5:
                return True
            else:
                return False

    def modificar(self, nombre, anio, mes, mdia, hora, minu, recordado=None):
        """Modifica el recordatorio (ya que todas las propiedades son
        variables de objeto esto es muy comodo)."""
        if recordado is not None:
            self.recordado = recordado
        self.nombre = nombre
        self.anio = anio
        self.mes = mes
        self.mdia = mdia
        self.hora = hora
        self.minu = minu

    def mostrar(self):
        """Devuelve una lista con todas las propiedades del recordatorio."""
        return [self.nombre, self.anio, self.mes,
                self.mdia, self.hora, self.minu, self.recordado]


class GestorLista:
    """Maneja todo lo que esta relacionado con la lista general en la que se
    guardan todos los recordatorios."""
    lista = []

    def __init__(self):
        pass

    def anadir(self, nombre, anio=t.tm_year, mes=t.tm_mon,
               mdia=t.tm_mday, hora=t.tm_hour, minu=0):
        """Anade un recordatorio a la lista de recordatorios.
        Si solo se le da el nombre como argumento pone todos los datos en los
        actuales y los minutos a 0.
        """
        self.lista.append(Recordatorio(nombre, anio, mes, mdia, hora, minu))

    def eliminar(self, pos):
        if pos == "*":
            self.lista = []
        else:
            self.lista.pop(pos)
