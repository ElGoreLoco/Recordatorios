from time import sleep, localtime

import notificar
import config


def ejec(term=True):
    if config.recordar:
        while True:
            sleep(config.actualizar_cada)
            if notificar.ejec():
                print("Recordatorio recordado! " + str(localtime()[:]))
