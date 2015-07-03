import sqlite3

db = sqlite3.connect('recordatorios/db/recordatorios.db')
cursor = db.cursor()


def cargar(recordatorios):
    """Almacena los recordatorios que estan en la base de datos."""
    recordatorios.eliminar("*")

    cursor.execute("SELECT * FROM recordatorios")
    recordatoriosLista = cursor.fetchall()

    for i in recordatoriosLista:
        recordatorios.anadir(i[0], i[1], i[2], i[3], i[4], i[5])


def guardar(recordatorios):
    """Guarda los recordatorios en la base de datos."""
    cursor.execute("DELETE FROM recordatorios")
    db.commit()

    recordatoriosG = []

    for i in range(0, len(recordatorios.lista)):
        recordatoriosG.append(recordatorios.lista[i].mostrar())

    for i in recordatoriosG:
        try:
            cursor.execute("INSERT INTO recordatorios VALUES(?,?,?,?,?,?,?)", i)
            db.commit()
        except sqlite3.IntegrityError:
            print("Ya hay un recordatorio con ese nombre.")
